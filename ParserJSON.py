#!/usr/bin/python

import sys, string, json, UIObjects

from SwiftGenerator import SwiftGenerator

from jsonspec.validators import load

theme = json.loads(open("Theme.json").read())
schema = json.loads(open("Theme.schema.json").read())

# data will validate against this schema
validator = load(schema)

# validate this data
validator.validate(theme)

class ParserJSON:

    swiftGenerator = SwiftGenerator()
    ui = UIObjects

    file = open("Theme.swift", "w+")
    swiftGenerator.timestamp()
    swiftGenerator.openClass()

    if 'Fonts' in theme:
        fontDefinitions = theme['Fonts']
        swiftGenerator.buildFontConstants(fontDefinitions)

    if 'Colors' in theme:
        colorDefinitions = theme['Colors']
        swiftGenerator.buildColorConstants(colorDefinitions)

    if 'Images' in theme:
        imageDefinitions = theme['Images']
        swiftGenerator.buildImageConstants(imageDefinitions)

    if 'Labels' in theme:
        for key, value in theme['Labels'].iteritems():
            Label = ui.uiObject(key + "Label", "UILabel")
            swiftGenerator.labelOutletCollections([Label])

    if 'Buttons' in theme:
        for key, value in theme['Buttons'].iteritems():
            object = ui.uiObject(key + "Button", "UIButton")
            swiftGenerator.buttonOutletCollections([object])

    if 'TextFields' in theme:
        for key, value in theme['TextFields'].iteritems():
            object = ui.uiObject(key + "TextField", "UITextField")
            swiftGenerator.textFieldOutletCollection([object])

    for key, value in theme['Labels'].iteritems():
        object = ui.uiObject(key + "Label", "UILabel")
        if "font" in value:
            object.font = ui.Font(value['font'], value['size'])
        if "textColor" in value:
            object.textColor = (value['textColor'])
        swiftGenerator.buildStyleFunctions([object])

    for key, value in theme['Buttons'].iteritems():
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
        swiftGenerator.buildStyleFunctions([object])

    for key, value in theme['TextFields'] .iteritems():
        object = ui.uiObject(key + "TextField", "UITextField")
        if "backgroundColor" in value:
            object.backgroundColor = value['backgroundColor']
        if "borderColor" in value:
            object.borderColor = value['borderColor']
        if "borderWidth" in value:
            object.borderWidth = value['borderWidth']
        if "textColor" in value:
            object.textColor = (value['textColor'])
        swiftGenerator.buildStyleFunctions([object])


    swiftGenerator.closeClass()

    ## write and close file
    file.write(swiftGenerator.end())
    file.close()
    print swiftGenerator.end()
