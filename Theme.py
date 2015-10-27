import sys, string, UIObjects
from SwiftGenerator import SwiftGenerator

swiftGenerator = SwiftGenerator()
ui = UIObjects
file = open("Theme.swift", "w+")
swiftGenerator.timestamp()

# ## define Color ##
# lightColor = ui.Color(1, 1, 1, 1)
# tertiaryColor = ui.Color(1, 1, 0 ,1)
# buttonPrimaryColor = ui.Color(0, 0, 1, 1)
# greyColor = ui.Color(224,224,224, 1)
# darkColor = ui.Color(0, 0, 0, 1)
#
# ## define Font ##
# lightFont = ui.Font("BrandonGrotesque-Light")
# mediumFont = ui.Font("BrandonGrotesque-Medium")
# boldFont = ui.Font("BrandonGrotesque-Bold")
# blackFont = ui.Font("BrandonGrotesque-Black")
#
# H7Label = ui.Label("H7Label")
# H7Label.font = ui.Font(lightFont.name)
# H7Label.font.size = 20
# H7Label.setTextColor(lightColor.toSwiftRGBA())
#
# H2Label = ui.Label("H2Label")
# H2Label.font = ui.Font(mediumFont.name)
# H2Label.font.size = 24
# H2Label.setTextColor(darkColor.toSwiftRGBA())
#
# H3Label = ui.Label("H3Label")
# H3Label.font = ui.Font(mediumFont.name)
# H3Label.font.size = 14
# H3Label.setTextColor(tertiaryColor.toSwiftRGBA())
#
# B1Button = ui.Button("B1Button")
# B1Button.titleColor = ui.Color(1, 0, 0, 1)
# B1Button.setBackgroundColor(buttonPrimaryColor.toSwiftRGBA())
# B1Button.setTitleColor(lightColor.toSwiftRGBA())
#
# B2Button = ui.Button("B2Button")
# B2Button.setBackgroundColor(lightColor.toSwiftRGBA())
# B2Button.setCornerRadius(5)
# B2Button.setBorderColor(darkColor.toSwiftRGBA())
# B2Button.setBorderWidth(2)
#
# B3Button = ui.Button("B3Button")
# B3Button.setTitleColor(darkColor.toSwiftRGBA())
# B3Button.setBackgroundColor(greyColor.toSwiftRGBA())
# B3Button.setCornerRadius(10)
# B3Button.setBorderColor(darkColor.toSwiftRGBA())
# B3Button.setBorderWidth(2)

## begin swift generation ##
swiftGenerator.openClass()
# swiftGenerator.labelOutletCollections([H7Label])
# swiftGenerator.buttonOutletCollections([B1Button, B2Button, B3Button])
# swiftGenerator.buildLabelStyleFunctions([H7Label])
# swiftGenerator.buildButtonStyleFunctions([B1Button, B2Button, B3Button])
swiftGenerator.buildStyleFunctions([Button])

swiftGenerator.closeClass()

## write and close file
file.write(swiftGenerator.end())
file.close()
print swiftGenerator.end()
