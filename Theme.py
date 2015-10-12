import sys, string, PyUI
from SwiftGenerator import SwiftGenerator

swiftGenerator = SwiftGenerator()
pyUI = PyUI
file = open("Theme.swift", "w+")
swiftGenerator.timestamp()

## define h1 ##
H1Font = pyUI.Font("Asul", 34)
H1Color = pyUI.Color(1, 0, 0, 1)
H1Label = pyUI.Label("H1Label")
H1Label.font = H1Font
H1Label.setTextColor(H1Color.toSwift())

## define h2 ##
H2Font = pyUI.Font("Asul", 24)
H2Color = pyUI.Color(0, 1, 0, 1)
H2Label = pyUI.Label("H2Label")
H2Label.font = H2Font
H2Label.setTextColor(H2Color.toSwift())

## define h3 ##
H3Font = pyUI.Font("Asul", 14)
H3Color = pyUI.Color(1, 0, 1, 1)
H3Label = pyUI.Label("H3Label")
H3Label.font = H3Font
H3Label.setTextColor(H3Color.toSwift())

## define button1 ##
Button1 = pyUI.Button("Button1")
Button1Color = pyUI.Color(0, 0, 1, 1)
Button1.setBackgroundColor(Button1Color.toSwift())

##define button2 ##
Button2 = pyUI.Button("Button2")
Button2Color = pyUI.Color(1, 1, 0, 1)
Button2.setBackgroundColor(Button2Color.toSwift())

## begin swift generation ##
swiftGenerator.openClass()
swiftGenerator.labelOutletCollections([H1Label, H2Label, H3Label])
swiftGenerator.buttonOutletCollections([Button1, Button2])
swiftGenerator.buildLabelStyleFunctions([H1Label, H2Label, H3Label])
swiftGenerator.buildButtonStyleFunctions([Button1, Button2])
swiftGenerator.closeClass()

## write and close file
file.write(swiftGenerator.end())
file.close()
print swiftGenerator.end()
