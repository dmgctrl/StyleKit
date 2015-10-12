import sys, string

class Label:
    def __init__(self, name):
        self.name = name
        self.textColor = None
        self.font = None
        
    def setTextColor(self, textColor):
        self.textColor = textColor

class Button:
    def __init__(self, name):
        self.name = name
        self.tintColor = None

    def setTintColor(self, tintColor):
        self.tintColor = tintColor

class Font:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def toSwift(self):
        return "UIFont (name: \"%s\", size: %s)" % (self.name, self.size)

class Color:
    
    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
        
    def toSwift(self):
        return "UIColor(red: %.2f, green: %.2f, blue: %.2f, alpha: %.2f)" % (self.red, self.green, self.blue, self.alpha)

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

    def labelOutletCollection(self, label):
        self.write(self.iboutlet + label.name + ": "+ self.labelArray + "{" )
        self.indent()
        self.newline()
        self.didSet(label.name)
        self.newline()
        self.outdent()
        self.write("}")
        self.newline()
        self.newline()

    def buttonOutletCollection(self, button):
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
       
    def buildLabelStyleFunction(self, label):
        self.write("func " + "style" + label.name + self.labelArgument + " {" )
        self.newline()
        self.indent()
        self.write("for object in " + label.name + " {")
        self.newline()
        self.indent()
        if label.font: set([self.write("object.font = " + label.font.toSwift())]),  self.newline()
        if label.textColor: set([self.write("object.textColor = " + label.textColor)]), self.newline()
        self.indent()
        self.write("}")
        self.newline()
        self.outdent()
        self.outdent()
        self.write("}")

    def buildButtonStyleFunction(self, button):
        self.write("func " + "style" + button.name + self.buttonArgument + " {" )
        self.newline()
        self.indent()
        self.write("}")

 
    def write(self, string):
        self.code.append(self.tab * self.level + string)
        
    def indent(self):
        self.level = self.level + 1

    def outdent(self):
        if self.level == 0:
            raise SyntaxError, "internal error in code generator"
        self.level = self.level - 1

    def newFunction(self):
        self.outdent()
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
file = open("Theme.swift", "w")

## define h1 ##
H1Font = Font("Asul", 34)
H1Color = Color(1, 0, 0, 1)
H1Label = Label("H1Label")
H1Label.font = H1Font
H1Label.setTextColor(H1Color.toSwift())

## define h2 ##
H2font = Font("Asul", 24)
H2Color = Color(0, 1, 0, 1)
H2Label = Label("H2Label")
H2Label.font = H2font
H2Label.setTextColor(H2Color.toSwift())

## define button1 ##
Button1 = Button("Button1")
Button1Color = Color(0, 0, 1, 1)
Button1.tintColor = Button1Color


## begin swift generation ##
swiftGenerator.begin(tab="    ")
swiftGenerator.openClass()
swiftGenerator.labelOutletCollection(H1Label)
swiftGenerator.labelOutletCollection(H2Label)
swiftGenerator.buttonOutletCollection(Button1)
swiftGenerator.buildLabelStyleFunction(H1Label)
swiftGenerator.newFunction()
swiftGenerator.buildButtonStyleFunction(Button1)
swiftGenerator.newFunction()
swiftGenerator.buildLabelStyleFunction(H2Label)
swiftGenerator.closeClass()
file.write(swiftGenerator.end())
file.close()
print swiftGenerator.end()