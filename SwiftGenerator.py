import sys, string, UIObjects, datetime, time

class SwiftGenerator:

    def __init__(self):
        self.code = []
        self.tab = "    "
        self.indentLevel = 0
        self.iboutlet = "@IBOutlet var "
        self.labelArray = "[UILabel]! "
        self.viewArray = "[UIView]! "
        self.buttonArray = "[UIButton]! "
        self.textFieldArray = "[UITextField]! "
        self.segmentedControlArray = "[UISegmentedControl]! "
        self.ui = UIObjects
        self.clearBackground = "object.backgroundColor = UIColor.clearColor()"
        self.attributeDictionary = " Dictionary<String, AnyObject>"
        self.seperator = ","
        self.unwrap = "!"

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
            if 'alpha' in value:
                alpha = value['alpha']
            else:
                alpha = 1.0
            if 'hex' in value:
                color = self.ui.HexColor(value['hex'], alpha)
            else:
                color = self.ui.RGBColor(value['red'], value['green'], value['blue'], alpha)

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

    def viewOutletCollections(self, views = []):
        for view in views:
            self.write(self.iboutlet + view.name + ": "+ self.viewArray + "{" )
            self.enter()
            self.didSet(view.name)
            self.closeCollection()

    def buttonOutletCollections(self, buttons = []):
        for button in buttons:
            self.write(self.iboutlet + button.name + ": "+ self.buttonArray + "{" )
            self.enter()
            self.didSet(button.name)
            self.closeCollection()

    def textFieldOutletCollection(self, textfields = []):
        for textfield in textfields:
            self.write(self.iboutlet + textfield.name + ": "+ self.textFieldArray + "{" )
            self.enter()
            self.didSet(textfield.name)
            self.closeCollection()

    def segmentedControlOutletCollection(self, segmentedControls = []):
        for segmentedControl in segmentedControls:
            self.write(self.iboutlet + segmentedControl.name + ": "+ self.segmentedControlArray + "{" )
            self.enter()
            self.didSet(segmentedControl.name)
            self.closeCollection()
        
    def didSet(self, name):
        self.write("didSet {")
        self.enter()
        self.write("style" + name + "("+ name +")")
        self.newline()
        self.outdent()
        self.write("}")

    def buildStyleFunctions(self, objects = []):
        for object in objects:
            self.write("func style" + object.name + "(objects: [" + object.type + "]) {")
            self.enter()
            self.write("for object in objects {")
            self.newline()
            self.indent()
            if isinstance(object, UIObjects.View):
                if object.backgroundColor: set([self.write("object.backgroundColor = " + object.backgroundColor)]), self.newline()
                if object.cornerRadius: set([self.write("object.layer.cornerRadius = " + str(object.cornerRadius))]), self.newline()
                if object.borderColor: set([self.write("object.layer.borderColor = " + object.borderColor + ".CGColor")]), self.newline()
                if object.borderWidth: set([self.write("object.layer.borderWidth = " + str(object.borderWidth))]), self.newline()

            if isinstance(object, UIObjects.Label):
                if object.textColor: set([self.write("object.textColor = " + object.textColor)]), self.newline()
                if object.fontStyle: set([self.write("object.font = " + object.fontStyle.toSwift())]),  self.newline()
                if object.textAlignment: set([self.write("object.textAlignment = NSTextAlignment." + object.textAlignment)]), self.newline()

            if isinstance(object, UIObjects.Button):
                if object.titleColorNormal: set([self.write("object.setTitleColor(" + object.titleColorNormal + ", forState: .Normal)")]), self.newline()
                if object.titleColorSelected: set([self.write("object.setTitleColor(" + object.titleColorSelected + ", forState: .Selected)")]), self.newline()
                if object.titleColorHighlighted: set([self.write("object.setTitleColor(" + object.titleColorHighlighted + ", forState: .Highlighted)")]), self.newline()
                if object.fontStyle: set([self.write("object.titleLabel?.font = " + object.fontStyle.toSwift())]), self.newline()
                if object.titleShadowColor: set([self.write("object.setTitleShadowColor(" + object.titleShadowColor + ", forState: .Normal)")]),self.newline()
                if object.backgroundImage: set([self.write("object.setBackgroundImage(" + object.backgroundImage + ", forState: .Normal)",)]),self.newline(), self.write(self.clearBackground),self.newline()
                if object.attributes:
                    if object.attributes.normal:
                        set([self.write("object.setTitleTextAttributes(normalAttributesFor" + object.name + "(), forState: .Normal)")]), self.newline()
                    if object.attributes.highlighted:
                        set([self.write("object.setTitleTextAttributes(highlightedAttributesFor" + object.name + "(), forState: .Highlighted)")]), self.newline()

            if isinstance(object, UIObjects.TextField):
                if object.textColor: set([self.write("object.textColor = " + object.textColor)]), self.newline()
                if object.fontStyle: set([self.write("object.font = " + object.fontStyle.toSwift())]),  self.newline()
                if object.textAlignment: set([self.write("object.textAlignment = NSTextAlignment." + object.textAlignment)]), self.newline()
                if object.borderStyle: set([self.write("object.borderStyle = UITextBorderStyle." + object.borderStyle)]), self.newline()

            if isinstance(object, UIObjects.SegmentedControl):
                if object.normalColor: set([self.write("object.setBackgroundImage(UIImage.imageWithColor(" + object.normalColor + "), forState: .Normal, barMetrics: .Default)")]), self.newline()
                if object.selectedColor: set([self.write("object.setBackgroundImage(UIImage.imageWithColor(" + object.selectedColor + "), forState: .Selected, barMetrics: .Default)")]), self.newline()
                if object.dividerColor: set([self.write("object.setDividerImage(UIImage.imageWithColor(" + object.dividerColor + "), forLeftSegmentState: .Normal, rightSegmentState: .Normal, barMetrics: .Default)")]), self.newline()
                if object.attributes:
                    if object.attributes.normal:
                        set([self.write("object.setTitleTextAttributes(attributesFor" + object.name + "(), forState: .Normal)")]), self.newline()
                    if object.attributes.selected:
                        set([self.write("object.setTitleTextAttributes(attributesFor" + object.name + "(), forState: .Selected)")]), self.newline()

            self.write("}")
            self.closeFunction()
            self.nextFunction()

    def buildAttributesForObjects(self, objects = []):
        for object in objects:
            if object.normal:
                normalObject = object.normal
                self.write("func normalAttributesFor" + object.name + "() -> " + self.attributeDictionary + " { ")
                self.enter()
                self.write("let attributes = [ ")
                self.indent(),self.newline()
                if isinstance(normalObject, UIObjects.Normal):
                    normalObject.seperatorCount = len(normalObject.properties) - 1
                    if normalObject.fontStyle: set([self.write("NSFontAttributeName: " + normalObject.fontStyle.toSwift() + self.unwrap)]),self.addSeperator(normalObject),self.newline()
                    if normalObject.foregroundColor: set([self.write("NSForegroundColorAttributeName: " + normalObject.foregroundColor)]),self.addSeperator(normalObject),self.newline()
                    if normalObject.backgroundColor: set([self.write("NSBackgroundColorAttributeName: " + normalObject.backgroundColor)]),self.addSeperator(normalObject),self.newline()
                    if normalObject.kerning: set([self.write("NSKernAttributeName: " + str(normalObject.kerning))]),self.addSeperator(normalObject),self.newline()
                    if normalObject.ligature: set([self.write("NSLigatureAttributeName: " + str(normalObject.ligature))]),self.addSeperator(normalObject),self.newline()
                self.outdent()
                self.write(" ]")
                self.newline()
                self.write("return attributes")
                self.closeFunction()
                self.nextFunction()
            if object.selected:
                selectedObject = object.selected
                self.write("func selectedAttributesFor" + selectedObject.name + "() -> " + self.attributeDictionary + " { ")
                self.enter()
                self.write("let attributes = [ ")
                self.indent(),self.newline()
                if isinstance(selectedObject, UIObjects.Selected):
                    selectedObject.seperatorCount = len(selectedObject.properties) - 1
                    if selectedObject.font: set([self.write("NSFontAttributeName: " + selectedObject.fontStyle.toSwift() + self.unwrap)]),self.addSeperator(selectedObject),self.newline()
                    if selectedObject.foregroundColor: set([self.write("NSForegroundColorAttributeName: " + selectedObject.foregroundColor)]),self.addSeperator(selectedObject),self.newline()
                    if selectedObject.backgroundColor: set([self.write("NSBackgroundColorAttributeName: " + selectedObject.backgroundColor)]),self.addSeperator(selectedObject),self.newline()
                    if selectedObject.kerning: set([self.write("NSKernAttributeName: " + str(selectedObject.kerning))]),self.addSeperator(selectedObject),self.newline()
                    if selectedObject.ligature: set([self.write("NSLigatureAttributeName: " + str(selectedObject.ligature))]),self.addSeperator(selectedObject),self.newline()
                self.outdent()
                self.write(" ]")
                self.newline()
                self.write("return attributes")
                self.closeFunction()
                self.nextFunction()
            if object.highlighted:
                highlightedObject = object.highlighted
                self.write("func highlightedAttributesFor" + highlightedObject.name + "() -> " + self.attributeDictionary + " { ")
                self.enter()
                self.write("let attributes = [ ")
                self.indent(),self.newline()
                if isinstance(highlightedObject, UIObjects.Highlighted):
                    highlightedObject.seperatorCount = len(selectedObject.properties) - 1
                    if highlightedObject.font: set([self.write("NSFontAttributeName: " + highlightedObject.fontStyle.toSwift() + self.unwrap)]),self.addSeperator(highlightedObject),self.newline()
                    if highlightedObject.foregroundColor: set([self.write("NSForegroundColorAttributeName: " + highlightedObject.foregroundColor)]),self.addSeperator(highlightedObject),self.newline()
                    if highlightedObject.backgroundColor: set([self.write("NSBackgroundColorAttributeName: " + highlightedObject.backgroundColor)]),self.addSeperator(highlightedObject),self.newline()
                    if highlightedObject.kerning: set([self.write("NSKernAttributeName: " + str(highlightedObject.kerning))]),self.addSeperator(highlightedObject),self.newline()
                    if highlightedObject.ligature: set([self.write("NSLigatureAttributeName: " + str(highlightedObject.ligature))]),self.addSeperator(highlightedObject),self.newline()
                self.outdent()
                self.write(" ]")
                self.newline()
                self.write("return attributes")
                self.closeFunction()
                self.nextFunction()

    def addSeperator(self, object):
        count = object.seperatorCount
        if count > 0:
            self.append(self.seperator)
            count = count - 1
            object.seperatorCount = count

    def append(self, string):
        self.code.append(string)

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
        self.newline()
        self.outdent()
        self.write("}")

    def openClass(self):
        self.write("import UIKit\n")
        self.newline()
        self.write("class Style: NSObject {\n")
        self.newline()
        self.indent()
        self.write("static let sharedInstance = Style()")
        self.newline()
        self.newline()

    def closeCollection(self):
        self.newline()
        self.outdent()
        self.write("}")
        self.newline()
        self.newline()

    def closeClass(self):
        self.indentLevel = 0
        self.write("}")
