#!/usr/bin/python

import sys, getopt, string, json, UIObjects

from SwiftGenerator import SwiftGenerator
from jsonschema import validators

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print 'ParseJSON.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'ParseJSON.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print 'Input file is "', inputfile
    print 'Output file is "', outputfile

    style = json.loads(open(inputfile).read())

    validators.validate(style, {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "Fonts": {
                "type": "object",
                "patternProperties": {
                    "^.*$": {"$ref": "#/definitions/bundleKey"}
                }
            },
            "Colors": {
                "type": "object",
                "patternProperties": {
                    "^.*$": {
                        "type": "object",
                        "pattern": "^[a-zA-Z0-9\-\_]+$",
                        "properties": {
                            "red": {"$ref": "#/definitions/colorValue"},
                            "green": {"$ref": "#/definitions/colorValue"},
                            "blue": {"$ref": "#/definitions/colorValue"},
                            "alpha": {"$ref": "#/definitions/alphaValue"}
                        },
                        "required": ["red", "green", "blue", "alpha"]
                    }
                }
            },
            "Images": {
                "type": "object",
                "patternProperties": {
                    "^.*$": {"$ref": "#/definitions/bundleKey"}
                }
            },
            "Labels": {
                "type": "object",
                "patternProperties": {
                    "^.*$": {
                        "type": "object",
                        "properties": {
                            "font": {"type": "string"},
                            "size": {"type": "integer"},
                            "color": {"type": "string"}
                        },
                        "required": ["font", "size"]
                    }
                }
            },
            "Buttons": {
                "type": "object",
                "patternProperties": {
                    "^.*$": {
                        "type": "object",
                        "properties": {
                            "titleLabelFont": {"type": "string"},
                            "size": {"type": "integer"},
                            "backgroundColor": {"type": "string"},
                            "cornerRadius": {"type": "integer"},
                            "normal": {"$ref": "#/definitions/buttonState"},
                            "highlighted": {"$ref": "#/definitions/buttonState"},
                            "selected": {"$ref": "#/definitions/buttonState"}
                        },
                        "required": ["titleLabelFont", "size"]
                    }
                }
            },
            "TextFields": {
                "type": "object",
                "patternProperties": {
                    "^.*$": {
                        "type": "object",
                        "properties": {
                            "attributes": {"type": "object"},
                            "textColor": {"type": "string"},
                            "backgroundColor": {"type": "string"},
                            "borderColor": {"type": "string"},
                            "borderWidth": {"type": "integer"},
                            "cornerRadius": {"type": "integer"},
                            "textAlignment": {
                                "enum": [
                                    "Left",
                                    "Right",
                                    "Center",
                                    "Justified",
                                    "Natural"
                                ]
                            },
                            "borderStyle": {
                                "enum": [
                                    "None",
                                    "Line",
                                    "Bezel",
                                    "RoundedRect"
                                ]
                            }
                        }
                    }
                }
            }
        },
        "definitions": {
            "bundleKey": {
                "type": "string",
                "pattern": "^[a-zA-Z0-9\-\_]+$"
            },
            "colorValue": {
                "type": "integer",
                "minimum": 0,
                "maximum": 255
            },
            "alphaValue": {
                "type": "number",
                "minimum": 0.0,
                "maximum": 1.0
            },
            "buttonState": {
                "properties": {
                    "titleColor": {
                        "type": "string",
                        "pattern": "^[a-zA-Z0-9]+$"
                    },
                    "titleShadowColor": {
                        "type": "string",
                        "pattern": "^[a-zA-Z0-9]+$"
                    }
                }
            }
        }
    })

    swiftGenerator = SwiftGenerator()
    ui = UIObjects

    file = open(outputfile, "w+")
    swiftGenerator.openClass()

    if 'Fonts' in style:
        fontDefinitions = style['Fonts']
        swiftGenerator.buildFontConstants(fontDefinitions)

    if 'Colors' in style:
        colorDefinitions = style['Colors']
        swiftGenerator.buildColorConstants(colorDefinitions)

    if 'Images' in style:
        imageDefinitions = style['Images']
        swiftGenerator.buildImageConstants(imageDefinitions)

    if 'Labels' in style:
        for key, value in style['Labels'].iteritems():
            Label = ui.uiObject(key + "Label", "UILabel")
            swiftGenerator.labelOutletCollections([Label])

    if 'Buttons' in style:
        for key, value in style['Buttons'].iteritems():
            object = ui.uiObject(key + "Button", "UIButton")
            swiftGenerator.buttonOutletCollections([object])

    if 'TextFields' in style:
        for key, value in style['TextFields'].iteritems():
            object = ui.uiObject(key + "TextField", "UITextField")
            swiftGenerator.textFieldOutletCollection([object])

    for key, value in style['Labels'].iteritems():
        object = ui.uiObject(key + "Label", "UILabel")
        if "font" in value:
            object.font = ui.Font(value['font'], value['size'])
        if "backgroundColor" in value:
            object.backgroundColor = (value['backgroundColor'])
        if "textColor" in value:
            object.textColor = (value['textColor'])
        if "attributes" in value:
            attributes = value["attributes"]
            object.seperatorCount = len(attributes) - 2
            if "font" in attributes:
                object.attributedFont = ui.Font(attributes['font'], attributes['size'])
                object.attributes.append(attributes['font'])
            if "foregroundColor" in attributes:
                object.attributedForegroundColor = attributes['foregroundColor']
                object.attributes.append(attributes['foregroundColor'])
            if "backgroundColor" in attributes:
                object.attributedBackgroundColor = attributes['backgroundColor']
                object.attributes.append(attributes['backgroundColor'])
            if "kern" in attributes:
                object.attributedKerning = attributes['kern']
                object.attributes.append(attributes['kern'])
            if "ligature" in attributes:
                object.attributedLigature = attributes['ligature']
                object.attributes.append(attributes['ligature'])
            swiftGenerator.buildAttributesForObjects([object])
        swiftGenerator.buildStyleFunctions([object])

    for key, value in style['Buttons'].iteritems():
        object = ui.uiObject(key + "Button", "UIButton")
        if "backgroundColor" in value:
            object.backgroundColor = (value['backgroundColor'])
        if "titleLabelFont" in value:
            object.titleLabel = ui.Font(value['titleLabelFont'], value['size'])
        if "cornerRadius" in value:
            object.cornerRadius = value['cornerRadius']
        if "borderColor" in value:
            object.borderColor = value['borderColor']
        if "borderWidth" in value:
            object.borderWidth = value['borderWidth']
        if "normal" in value:
            normal = value["normal"]
            if "titleColor" in normal:
                object.titleColor = (normal['titleColor'])
            if "backgroundImage" in normal:
                object.backgroundImage = normal['backgroundImage']
        if "highlighted" in value:
            highlighted = value["highlighted"]
        if "disabled" in value:
            print("disabled")
        if "selected" in value:
            print("selected")
        if "application" in value:
            print("application")
        if "reserved" in value:
            print ("reserved")
        if "attributes" in value:
            attributes = value["attributes"]
            object.seperatorCount = len(attributes) - 2
            if "font" in attributes:
                object.attributedFont = ui.Font(attributes['font'], attributes['size'])
                object.attributes.append(attributes['font'])
            if "foregroundColor" in attributes:
                object.attributedForegroundColor = attributes['foregroundColor']
                object.attributes.append(attributes['foregroundColor'])
            if "backgroundColor" in attributes:
                object.attributedBackgroundColor = attributes['backgroundColor']
                object.attributes.append(attributes['backgroundColor'])
            if "kern" in attributes:
                object.attributedKerning = attributes['kern']
                object.attributes.append(attributes['kern'])
            if "ligature" in attributes:
                object.attributedLigature = attributes['ligature']
                object.attributes.append(attributes['ligature'])
            swiftGenerator.buildAttributesForObjects([object])
        swiftGenerator.buildStyleFunctions([object])

    for key, value in style['TextFields'].iteritems():
        object = ui.uiObject(key + "TextField", "UITextField")
        if "backgroundColor" in value:
            object.backgroundColor = value['backgroundColor']
        if "borderColor" in value:
            object.borderColor = value['borderColor']
        if "borderWidth" in value:
            object.borderWidth = value['borderWidth']
        if "textColor" in value:
            object.textColor = value['textColor']
        if "cornerRadius" in value:
            object.cornerRadius = value['cornerRadius']
        if "attributes" in value:
            attributes = value["attributes"]
            object.seperatorCount = len(attributes) - 2
            if "font" in attributes:
                object.attributedFont = ui.Font(attributes['font'], attributes['size'])
                object.attributes.append(attributes['font'])
            if "foregroundColor" in attributes:
                object.attributedForegroundColor = attributes['foregroundColor']
                object.attributes.append(attributes['foregroundColor'])
            if "backgroundColor" in attributes:
                object.attributedBackgroundColor = attributes['backgroundColor']
                object.attributes.append(attributes['backgroundColor'])
            if "kern" in attributes:
                object.attributedKerning = attributes['kern']
                object.attributes.append(attributes['kern'])
            if "ligature" in attributes:
                object.attributedLigature = attributes['ligature']
                object.attributes.append(attributes['ligature'])
            swiftGenerator.buildAttributesForObjects([object])

        swiftGenerator.buildStyleFunctions([object])

        swiftGenerator.closeClass()

        ## write and close file
        file.write(swiftGenerator.end())
        file.close()
        print swiftGenerator.end()

if __name__ == "__main__":
    main(sys.argv[1:])
