import sys, string

class Label:
    
    def __init__(self, name):
        self.name = name
        self.textColor = None
        self.font = None
        
    def setTextColor(self, textColor):
        self.textColor = textColor

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
        return "UIColor(red: %.2f, green: %f, blue: %.2f, alpha: %.2f)" % (self.red, self.green, self.blue, self.alpha)

class SwiftGenerator:
    
    def begin(self, tab="    "):
        self.code = []
        self.tab = tab
        self.level = 0
        self.iboutlet = "@IBOutlet var "
        self.labelArray = "[UILabel]! "
        self.buttonArray = "[UIButton]! "
  
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
        
    def didSet(self, name):
        self.write("didSet {")
        self.indent()
        self.newline()
        self.write(name + "Style()")
        self.newline()
        self.outdent()
        self.write("}")
       
    def buildLabelStyleFunction(self, label):
        self.write("func " + label.name +"Style() {")
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
        self.write("}")

 
    def write(self, string):
        self.code.append(self.tab * self.level + string)
        
    def indent(self):
        self.level = self.level + 1

    def outdent(self):
        if self.level == 0:
            raise SyntaxError, "internal error in code generator"
        self.level = self.level - 1





#################################################
swiftGenerator = SwiftGenerator()
file = open("Theme.swift", "w")

## define h1 ##
h1Font = Font("Asul", 34)
h1Color = Color(1, 0, 0, 1)
h1Label = Label("h1Label")
h1Label.font = h1Font
h1Label.setTextColor(h1Color.toSwift())

## define h2 ##
h2font = Font("Asul", 24)
h2Color = Color(0, 1, 0, 1)
h2Label = Label("h2Label")
h2Label.font = h2font
h2Label.setTextColor(h2Color.toSwift())

swiftGenerator.begin(tab="    ")
swiftGenerator.write("import UIKit\n")
swiftGenerator.newline()
swiftGenerator.write("class Theme: NSObject {\n")
swiftGenerator.newline()
swiftGenerator.indent()
swiftGenerator.labelOutletCollection(h1Label)
swiftGenerator.labelOutletCollection(h2Label)
swiftGenerator.buildLabelStyleFunction(h1Label)
swiftGenerator.outdent()
swiftGenerator.newline()
swiftGenerator.newline()
swiftGenerator.buildLabelStyleFunction(h2Label)
swiftGenerator.outdent()
swiftGenerator.newline()
swiftGenerator.outdent()
swiftGenerator.write("}")
file.write(swiftGenerator.end())
file.close()
print swiftGenerator.end()