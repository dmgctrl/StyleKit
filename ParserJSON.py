import sys, string, json, UIObjects
from SwiftGenerator import SwiftGenerator

class ParserJSON:

    theme = json.loads(open("Theme.json").read())
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
            Label = ui.Label(key + "Label")
            swiftGenerator.labelOutletCollections([Label])

    if 'Buttons' in theme:
        for key, value in theme['Buttons'].iteritems():
            Button = ui.Button(key + "Button")
            swiftGenerator.buttonOutletCollections([Button])

    for key, value in theme['Labels'].iteritems():
        Label = ui.Label(key + "Label")
        if "font" in value:
            Label.font = ui.Font(value['font'], value['size'])

        if "textColor" in value:
            Label.setTextColor(value['textColor'])
        swiftGenerator.buildLabelStyleFunctions([Label])

    for key, value in theme['Buttons'].iteritems():
        Button = ui.Button(key + "Button")
        if "backgroundColor" in value:
            Button.backgroundColor = (value['backgroundColor'])
        if "titleLabelFont" in value:
            Button.titleLabelFont = ui.Font(value['titleLabelFont'], value['size'])
        if "cornerRadius" in value:
            Button.cornerRadius = value['cornerRadius']
        if "borderColor" in value:
            Button.borderColor = value['borderColor']
        if "borderWidth" in value:
            Button.borderWidth = value['borderWidth']
        if "normal" in value:
            normal = value["normal"]
            if "titleColor" in normal:
                Button.titleColor = (normal['titleColor'])
            if "backgroundImage" in normal:
                Button.backgroundImage = normal['backgroundImage']
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
        swiftGenerator.buildButtonStyleFunctions([Button])

    swiftGenerator.closeClass()

    ## write and close file
    file.write(swiftGenerator.end())
    file.close()
    print swiftGenerator.end()
