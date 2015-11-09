#!/usr/bin/python

import sys, getopt, string, json, UIObjects

from SwiftGenerator import SwiftGenerator
from Validator import Validator

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

    validator = Validator()
    validator.validate(style)
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
        label = ui.Label(key + "Label", value)
        if label.attributes:
            attributes = value["attributes"]
            swiftGenerator.buildAttributesForObjects([label.attributes])
        swiftGenerator.buildStyleFunctions([label])

    for key, value in style['Buttons'].iteritems():
        button = ui.Button(key + "Button", value)
        if button.normal:
            normal = value["normal"]
            if "titleColor" in normal:
                button.titleColor = normal['titleColor']
            if "backgroundImage" in normal:
                button.backgroundImage = normal['backgroundImage']
        if button.selected:
            selected = value["selected"]
            if "titleColor" in selected:
                button.titleColor = selected['titleColor']
            if "backgroundImage" in selected:
                button.backgroundImage = selected['backgroundImage']
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
        if button.attributes:
            attributes = value["attributes"]
            swiftGenerator.buildAttributesForObjects([button.attributes])
        swiftGenerator.buildStyleFunctions([button])

    for key, value in style['TextFields'].iteritems():
        textfield = ui.TextField(key + "TextField", value)
        if "textColor" in value:
            object.textColor = value['textColor']
        if textfield.attributes:
            attributes = value["attributes"]
            swiftGenerator.buildAttributesForObjects([textfield.attributes])
        swiftGenerator.buildStyleFunctions([textfield])

        swiftGenerator.closeClass()

        ## write and close file
        file.write(swiftGenerator.end())
        file.close()
        print swiftGenerator.end()

if __name__ == "__main__":
    main(sys.argv[1:])