import sys, string, UIObjects
from SwiftGenerator import SwiftGenerator

swiftGenerator = SwiftGenerator()
ui = UIObjects
file = open("Theme.swift", "w+")
swiftGenerator.timestamp()

## define Color ##
primaryColor = ui.Color(1, 0, 0, 1)
secondaryColor = ui.Color(0, 1, 0, 1)
tertiaryColor = ui.Color(1, 1,0 ,1)
buttonPrimaryColor = ui.Color(0, 0, 1,1)
hex = ui.Color.rgb_to_hex(primaryColor, 1, 1, 1)
print (hex)


## define Font ##
primaryFont = ui.Font("Asul")

## define h1 ##
H1Label = ui.Label("H1Label")
H1Label.font = ui.Font(primaryFont.name)
H1Label.font.size = 34
H1Label.setTextColor(primaryColor.toSwiftRGBA())

## define h2 ##
H2Label = ui.Label("H2Label")
H2Label.font = ui.Font(primaryFont.name)
H2Label.font.size = 24
H2Label.setTextColor(secondaryColor.toSwiftRGBA())

## define h3 ##
H3Label = ui.Label("H3Label")
H3Label.font = ui.Font(primaryFont.name)
H3Label.font.size = 14
H3Label.setTextColor(tertiaryColor.toSwiftRGBA())

## define button1 ##
Button1 = ui.Button("Button1")
Button1TitleColor = ui.Color(1, 0, 0, 1)
Button1.setBackgroundColor(buttonPrimaryColor.toSwiftRGBA())
Button1.setTitleColor(primaryColor.toSwiftRGBA())

##define button2 ##
Button2 = ui.Button("Button2")
Button2.setBackgroundColor(secondaryColor.toSwiftRGBA())

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
