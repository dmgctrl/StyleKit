import sys, string, PyUI

class SwiftGenerator:
    
    def begin(self, tab="    "):
        self.code = []
        self.tab = tab
        self.level = 0
        self.iboutlet = "@IBOutlet var "
        self.labelArray = "[UILabel]! "
        self.buttonArray = "[UIButton]! "
        self.labelArgument = "(labels: [UILabel])"
        self.buttonArgument = "(buttons: [UIButton])"
  
    def end(self):
        return string.join(self.code, "")
        
    def newline(self):
        self.write("\n")

    def labelOutletCollections(self, labels = []):
        for label in labels:
            self.write(self.iboutlet + label.name + ": "+ self.labelArray + "{" )
            self.indent()
            self.newline()
            self.didSet(label.name)
            self.newline()
            self.outdent()
            self.write("}")
            self.newline()
            self.newline()

    def buttonOutletCollections(self, buttons = []):
        for button in buttons:
            self.write(self.iboutlet + button.name + ": "+ self.buttonArray + "{" )
            self.indent()
            self.newline()
            self.didSet(button.name)
            self.newline()
            self.outdent()
            self.write("}")
            self.newline()
            self.newline()
        
    def didSet(self, name):
        self.write("didSet {")
        self.indent()
        self.newline()
        self.write("style" + name + "("+ name +")")
        self.newline()
        self.outdent()
        self.write("}")
       
    def buildLabelStyleFunctions(self, labels = []):
        for label in labels:
            self.write("func " + "style" + label.name + self.labelArgument + " {" )
            self.newline()
            self.indent()
            self.write("for object in " + label.name + " {")
            self.newline()
            self.indent()
            if label.font: set([self.write("object.font = " + label.font.toSwift())]),  self.newline()
            if label.textColor: set([self.write("object.textColor = " + label.textColor)]), self.newline()
            self.write("}")
            self.newline()
            self.outdent()
            self.write("}")
            self.nextFunction()



    def buildButtonStyleFunctions(self, buttons = []):
        for button in buttons:
            self.write("func " + "style" + button.name + self.buttonArgument + " {" )
            self.newline()
            self.indent()
            self.write("for object in " + button.name + " {")
            self.newline()
            self.indent()
            if button.backgroundColor: set([self.write("object.backgroundColor = " + button.backgroundColor)]), self.newline()


 
    def write(self, string):
        self.code.append(self.tab * self.level + string)
        
    def indent(self):
        self.level = self.level + 1

    def outdent(self):
        if self.level == 0:
            raise SyntaxError, "internal error in code generator"
        self.level = self.level - 1

    def nextFunction(self):
        self.level = 0
        ##self.outdent()
        self.newline()
        self.newline()

    def openClass(self):
        self.write("import UIKit\n")
        self.newline()
        self.write("class Theme: NSObject {\n")
        self.newline()
        self.indent()


    def closeClass(self):
        self.outdent()
        self.newline()
        self.outdent()
        self.write("}")



#################################################
swiftGenerator = SwiftGenerator()
pyUI = PyUI
file = open("Theme.swift", "w")

## define h1 ##
H1Font = pyUI.Font("Asul", 34)
H1Color = pyUI.Color(1, 0, 0, 1)
H1Label = pyUI.Label("H1Label")
H1Label.font = H1Font
H1Label.setTextColor(H1Color.toSwift())

## define h2 ##
H2font = pyUI.Font("Asul", 24)
H2Color = pyUI.Color(0, 1, 0, 1)
H2Label = pyUI.Label("H2Label")
H2Label.font = H2font
H2Label.setTextColor(H2Color.toSwift())

## define button1 ##
Button1 = pyUI.Button("Button1")
Button1Color = pyUI.Color(0, 0, 1, 1)
Button1.setBackgroundColor(Button1Color.toSwift())

##define button2 ##
Button2 = pyUI.Button("Button2")
Button2Color = pyUI.Color(1, 1, 0, 1)
Button2.setBackgroundColor(Button2Color.toSwift())

## begin swift generation ##
swiftGenerator.begin(tab="    ")
swiftGenerator.openClass()
swiftGenerator.labelOutletCollections([H1Label, H2Label])
swiftGenerator.buttonOutletCollections([Button1, Button2])
swiftGenerator.buildLabelStyleFunctions([H1Label, H2Label])
swiftGenerator.nextFunction()
swiftGenerator.buildButtonStyleFunctions([Button1, Button2])
swiftGenerator.closeClass()

file.write(swiftGenerator.end())
file.close()
print swiftGenerator.end()