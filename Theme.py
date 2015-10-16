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
buttonPrimaryColor = ui.Color(0, 0, 1, 1)
greyColor = ui.Color(224,224,224, 1)
darkColor = ui.Color(0, 0, 0, 1)

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
Button2.setCornerRadius(5)
Button2.setBorderColor(primaryColor.toSwiftRGBA())
Button2.setBorderWidth(2)

##define button3 ##
Button3 = ui.Button("Button3")
Button3.setTitleColor(darkColor.toSwiftRGBA())
Button3.setBackgroundColor(greyColor.toSwiftRGBA())
Button3.setCornerRadius(10)
Button3.setBorderColor(darkColor.toSwiftRGBA())
Button3.setBorderWidth(2)

## begin swift generation ##
swiftGenerator.openClass()
swiftGenerator.labelOutletCollections([H1Label, H2Label, H3Label])
swiftGenerator.buttonOutletCollections([Button1, Button2,Button3])
swiftGenerator.buildLabelStyleFunctions([H1Label, H2Label, H3Label])
swiftGenerator.buildButtonStyleFunctions([Button1, Button2, Button3])
swiftGenerator.closeClass()

## write and close file
file.write(swiftGenerator.end())
file.close()
print swiftGenerator.end()
