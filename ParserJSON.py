import sys, string, json, UIObjects
from SwiftGenerator import SwiftGenerator

class ParserJSON:
    theme = json.loads(open("Theme.json").read())
    swiftGenerator = SwiftGenerator()
    ui = UIObjects

    file = open("Theme.swift", "w+")
    swiftGenerator.timestamp()
    swiftGenerator.openClass()

    if 'Labels' in theme:
        for key, value in theme['Labels'].iteritems():
            Label = ui.Label(key + "Label")
            swiftGenerator.labelOutletCollections([Label])

        for key, value in theme['Labels'].iteritems():
            Label = ui.Label(key + "Label")
            if value['font']:
                Label.font = ui.Font(value['font'], value['size'])
                print(Label.name)
                swiftGenerator.buildLabelStyleFunctions([Label])
    else:
        print "No labels"

    swiftGenerator.closeClass()

    ## write and close file
    file.write(swiftGenerator.end())
    file.close()
    print swiftGenerator.end()