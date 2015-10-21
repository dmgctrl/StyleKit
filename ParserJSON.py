import sys, string, json, UIObjects
from SwiftGenerator import SwiftGenerator

class ParserJSON:
    theme = json.loads(open("Theme.json").read())
    print(theme)
    swiftGenerator = SwiftGenerator()
    ui = UIObjects

    file = open("Theme.swift", "w+")
    swiftGenerator.timestamp()
    swiftGenerator.openClass()

    if 'Fonts' in theme:
        fontDefinitions = theme['Fonts']
        swiftGenerator.buildFontConstants(fontDefinitions)

    if 'Labels' in theme:
        labelDefinitions = theme['Labels']
        for key, value in labelDefinitions.iteritems():
            Label = ui.Label(key + "Label")
            swiftGenerator.labelOutletCollections([Label])

        for key, value in labelDefinitions.iteritems():
            Label = ui.Label(key + "Label")
            if "font" in value:
                 Label.font = ui.Font(value['font'], value['size'])

            if "textColor" in value:
                Label.setTextColor(value['textColor'])
            swiftGenerator.buildLabelStyleFunctions([Label])
    else:
        print "No Labels Defined"

    swiftGenerator.closeClass()

    ## write and close file
    file.write(swiftGenerator.end())
    file.close()
    print swiftGenerator.end()
