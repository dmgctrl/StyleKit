#!/usr/bin/python

import UIObjects
import getopt
import json
import sys
from SwiftGenerator import SwiftGenerator
from Validator import Validator


def main(argv):
    inputfile = 'Style.json'
    outputfile = 'Style.swift'
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
    swiftgenerator = SwiftGenerator()
    ui = UIObjects

    _file = open(outputfile, "w+")
    swiftgenerator.openClass()

    if 'Fonts' in style:
        fontdefinitions = style['Fonts']
        swiftgenerator.buildFontConstants(fontdefinitions)

    if 'Colors' in style:
        colordefinitions = style['Colors']
        swiftgenerator.buildColorConstants(colordefinitions)

    if 'Images' in style:
        imagedefinitions = style['Images']
        swiftgenerator.buildImageConstants(imagedefinitions)

    if 'Labels' in style:
        for key, value in style['Labels'].iteritems():
            label = ui.uiObject(key + "Label", "UILabel")
            swiftgenerator.labelOutletCollections([label])

    if 'TextViews' in style:
        for key, value in style['TextViews'].iteritems():
            textView = ui.uiObject(key + "TextView", "UITextView")
            swiftgenerator.textViewOutletCollections([textView])

    if 'Views' in style:
        for key, value in style['Views'].iteritems():
            view = ui.uiObject(key + "View", "UIView")
            swiftgenerator.viewOutletCollections([view])

    if 'Buttons' in style:
        for key, value in style['Buttons'].iteritems():
            button = ui.uiObject(key + "Button", "UIButton")
            swiftgenerator.buttonOutletCollections([button])

    if 'TextFields' in style:
        for key, value in style['TextFields'].iteritems():
            textfield = ui.uiObject(key + "TextField", "UITextField")
            swiftgenerator.textFieldOutletCollection([textfield])

    if 'SegmentedControls' in style:
        for key, value in style['SegmentedControls'].iteritems():
            segmentedControl = ui.uiObject(key + "SegmentedControl", "UISegmentedControl")
            swiftgenerator.segmentedControlOutletCollection([segmentedControl])

    if 'Labels' in style:
        for key, value in style['Labels'].iteritems():
            label = ui.Label(key + "Label", value)
            if "textAlignment" in value:
                label.textAlignment = value['textAlignment']
            if "textColor" in value:
                label.textColor = value['textColor']
            if "lineSpacing" in value:
                label.lineSpacing = value['lineSpacing']
            if label.attributes:
                swiftgenerator.buildAttributesForObjects([label])
            swiftgenerator.buildStyleFunctions([label])

    if 'TextViews' in style:
        for key, value in style['TextViews'].iteritems():
            textView = ui.TextView(key + "TextView", value)
            if "textAlignment" in value:
                textView.textAlignment = value['textAlignment']
            if "textColor" in value:
                textView.textColor = value['textColor']
            if "lineSpacing" in value:
                textView.lineSpacing = value['lineSpacing']
            if textView.attributes:
                swiftgenerator.buildAttributesForObjects([textView])
            swiftgenerator.buildStyleFunctions([textView])

    if 'Views' in style:
        for key, value in style['Views'].iteritems():
            view = ui.View(key + "View", value)
            if "backgroundColor" in value:
                view.backgroundColor = value['backgroundColor']
            if "cornerRadius" in value:
                view.cornerRadius = value['cornerRadius']
            if "borderColor" in value:
                view.borderColor = value['borderColor']
            if "borderWidth" in value:
                view.borderWidth = value['borderWidth']
            swiftgenerator.buildStyleFunctions([view])

    if 'Buttons' in style:
        for key, value in style['Buttons'].iteritems():
            button = ui.Button(key + "Button", value)
            if "cornerRadius" in value:
                button.cornerRadius = value['cornerRadius']
            if "borderColor" in value:
                button.borderColor = value['borderColor']
            if "borderWidth" in value:
                button.borderWidth = value['borderWidth']
            if button.fontStyle:
                fontStyle = value["fontStyle"]
                button.font = fontStyle
            swiftgenerator.buildStyleFunctions([button])

    if 'TextFields' in style:
        for key, value in style['TextFields'].iteritems():
            textfield = ui.TextField(key + "TextField", value)
            if "textColor" in value:
                textfield.textColor = value['textColor']
            if "textAlignment" in value:
                textfield.textAlignment = value['textAlignment']
            if "borderStyle" in value:
                textfield.borderStyle = value['borderStyle']
            if textfield.fontStyle:
                fontStyle = value["fontStyle"]
                textfield.font = fontStyle
            swiftgenerator.buildStyleFunctions([textfield])

    if 'SegmentedControls' in style:
        for key, value in style['SegmentedControls'].iteritems():
            segmentedControl = ui.SegmentedControl(key + "SegmentedControl", value)
            if segmentedControl.fontStyle:
                fontStyle = value["fontStyle"]
                segmentedControl.font = fontStyle
            if "normalColor" in value:
                segmentedControl.normalColor = value['normalColor']
            if "selectedColor" in value:
                segmentedControl.selectedColor = value['selectedColor']
            if "dividerColor" in value:
                segmentedControl.dividerColor = value['dividerColor']
            swiftgenerator.buildStyleFunctions([segmentedControl])

        swiftgenerator.closeClass()

    # write and close file
    _file.write(swiftgenerator.end())
    _file.close()
    print swiftgenerator.end()


if __name__ == "__main__":
    main(sys.argv[1:])
