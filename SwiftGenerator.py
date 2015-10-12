import sys, string, PyUI, datetime, time

class SwiftGenerator:

    def __init__(self):
        self.code = []
        self.tab = "    "
        self.level = 0
        self.iboutlet = "@IBOutlet var "
        self.labelArray = "[UILabel]! "
        self.buttonArray = "[UIButton]! "
        self.labelArgument = "(labels: [UILabel])"
        self.buttonArgument = "(buttons: [UIButton])"

    def timestamp(self):
        ts = time.time()
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        self.write(timeStamp)
  
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
