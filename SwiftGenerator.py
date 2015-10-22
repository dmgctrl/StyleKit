import sys, string, UIObjects, datetime, time

class SwiftGenerator:

    def __init__(self):
        self.code = []
        self.tab = "    "
        self.indentLevel = 0
        self.iboutlet = "@IBOutlet var "
        self.labelArray = "[UILabel]! "
        self.buttonArray = "[UIButton]! "
        self.labelArgument = "(labels: [UILabel])"
        self.buttonArgument = "(buttons: [UIButton])"
        self.ui = UIObjects
        self.clearBackground = "object.backgroundColor = UIColor.clearColor()"

    def timestamp(self):
        ts = time.time()
        timeStamp = ("//Theme Generated:" + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        self.write(timeStamp)
        self.newline()
        self.newline()

    def end(self):
        return string.join(self.code, "")
        
    def newline(self):
        self.write("\n")

    def enter(self):
        self.indent()
        self.newline()

    def buildFontConstants(self, fontDefinitions = {}):
        for key, value in fontDefinitions.iteritems():
            self.write("let %s: String = \"%s\"" % (key, value))
            self.newline()
        self.newline()

    def buildColorConstants(self, colorDefinitions = {}):
        for key, value in colorDefinitions.iteritems():
            color = self.ui.Color(value['red'], value['green'],value['blue'],value['alpha'])
            self.write("let %s = %s" % (key, color.toSwiftRGBA()))
            self.newline()
        self.newline()

    def buildImageConstants(self, imageDefinitions = {}):
        for key, value in imageDefinitions.iteritems():
            image = self.write("let %s = UIImage(named: \"%s\")" % (key, value))
            self.newline()
        self.newline()

    def labelOutletCollections(self, labels = []):
        for label in labels:
            self.write(self.iboutlet + label.name + ": "+ self.labelArray + "{" )
            self.enter()
            self.didSet(label.name)
            self.closeCollection()

    def buttonOutletCollections(self, buttons = []):
        for button in buttons:
            self.write(self.iboutlet + button.name + ": "+ self.buttonArray + "{" )
            self.enter()
            self.didSet(button.name)
            self.closeCollection()
        
    def didSet(self, name):
        self.write("didSet {")
        self.enter()
        self.write("style" + name + "("+ name +")")
        self.newline()
        self.outdent()
        self.write("}")
       
    def buildLabelStyleFunctions(self, labels = []):
        for label in labels:
            self.write("func " + "style" + label.name + self.labelArgument + " {" )
            self.enter()
            self.write("for object in labels {")
            self.newline()
            self.indent()
            if label.font: set([self.write("object.font = " + label.font.toSwift())]),  self.newline()
            if label.textColor: set([self.write("object.textColor = " + label.textColor)]), self.newline()
            self.closeFunction()
            self.nextFunction()

    def buildButtonStyleFunctions(self, buttons = []):
        for button in buttons:
            self.write("func " + "style" + button.name + self.buttonArgument + " {" )
            self.enter()
            self.write("for object in buttons {")
            self.enter()
            if button.backgroundColor: set([self.write("object.backgroundColor = " + button.backgroundColor)]), self.newline()
            if button.titleColor: set([self.write("object.setTitleColor(" + button.titleColor + ", forState: .Normal)")]), self.newline()
            if button.titleLabelFont: set([self.write("object.titleLabel?.font = " + button.titleLabelFont.toSwift())]), self.newline()
            if button.cornerRadius: set([self.write("object.layer.cornerRadius = " + str(button.cornerRadius))]), self.newline()
            if button.borderColor: set([self.write("object.layer.borderColor = " + button.borderColor + ".CGColor")]), self.newline()
            if button.borderWidth: set([self.write("object.layer.borderWidth = " + str(button.borderWidth))]), self.newline()
            if button.titleShadowColor: set([self.write("object.setTitleShadowColor(" + button.titleShadowColor + ", forState: .Normal)")]),self.newline()
            if button.backgroundImage: set([self.write("object.setBackgroundImage(" + button.backgroundImage + ", forState: .Normal)")]),self.newline(), self.write(self.clearBackground),self.newline()
            self.closeFunction()
            self.nextFunction()

    def write(self, string):
        self.code.append(self.tab * self.indentLevel + string)
        
    def indent(self):
        self.indentLevel = self.indentLevel + 1

    def outdent(self):
        if self.indentLevel == 0:
            raise SyntaxError, "internal error in code generator"
        self.indentLevel = self.indentLevel - 1

    def nextFunction(self):
        self.indentLevel = 0
        self.enter()
        self.newline()

    def closeFunction(self):
        self.write("}")
        self.newline()
        self.outdent()
        self.write("}")

    def openClass(self):
        self.write("import UIKit\n")
        self.newline()
        self.write("class Theme: NSObject {\n")
        self.newline()
        self.indent()

    def closeCollection(self):
        self.newline()
        self.outdent()
        self.write("}")
        self.newline()
        self.newline()

    def closeClass(self):
        self.indentLevel = 0
        self.write("}")
