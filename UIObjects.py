class uiObject:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class View:
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def backgroundColor(self):
        if "backgroundColor" in self.properties:
            return (self.properties['backgroundColor'])
    @property
    def borderColor(self):
        if "borderColor" in self.properties:
            return (self.properties['borderColor'])

    @property
    def borderWidth(self):
        if "borderWidth" in self.properties:
            return (self.properties['borderWidth'])

    @property
    def cornerRadius(self):
        if "cornerRadius" in self.properties:
            return (self.properties['cornerRadius'])

    @property
    def type(self):
        return "UIView"

class FontStyle:
    def __init__(self, fontStyle):
        self.font = fontStyle["font"]
        self.size = fontStyle["size"]

    def toSwift(self):
        return "UIFont(name: %s, size: %s)" % (self.font, self.size)

class NormalState:
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def state(self):
        return ".Normal"

    @property
    def fontStyle(self):
        if "fontStyle" in self.properties:
            return FontStyle(self.properties['fontStyle'])

    @property
    def textColor(self):
        if "textColor" in self.properties:
            return (self.properties['textColor'])

    @property
    def foregroundColor(self):
        if "foregroundColor" in self.properties:
            return self.properties['foregroundColor']

    @property
    def backgroundColor(self):
        if "backgroundColor" in self.properties:
            return self.properties['backgroundColor']

    @property
    def backgroundImage(self):
        if "backgroundImage" in self.properties:
            return self.properties['backgroundImage']

    @property
    def titleShadowColor(self):
        if "titleShadowColor" in self.properties:
            return (self.properties['titleShadowColor'])

class HighlightedState:
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def state(self):
        return ".Highlighted"

    @property
    def fontStyle(self):
        if "fontStyle" in self.properties:
            return FontStyle(self.properties['fontStyle'])

    @property
    def textColor(self):
        if "textColor" in self.properties:
            return (self.properties['textColor'])

    @property
    def foregroundColor(self):
        if "foregroundColor" in self.properties:
            return self.properties['foregroundColor']

    @property
    def backgroundColor(self):
        if "backgroundColor" in self.properties:
            return self.properties['backgroundColor']

    @property
    def backgroundImage(self):
        if "backgroundImage" in self.properties:
            return self.properties['backgroundImage']

    @property
    def titleShadowColor(self):
        if "titleShadowColor" in self.properties:
            return (self.properties['titleShadowColor'])

class SelectedState:
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def state(self):
        return ".Selected"

    @property
    def fontStyle(self):
        if "fontStyle" in self.properties:
            return FontStyle(self.properties['fontStyle'])

    @property
    def textColor(self):
        if "textColor" in self.properties:
            return (self.properties['textColor'])

    @property
    def foregroundColor(self):
        if "foregroundColor" in self.properties:
            return self.properties['foregroundColor']

    @property
    def backgroundColor(self):
        if "backgroundColor" in self.properties:
            return self.properties['backgroundColor']

    @property
    def backgroundImage(self):
        if "backgroundImage" in self.properties:
            return self.properties['backgroundImage']

    @property
    def titleShadowColor(self):
        if "titleShadowColor" in self.properties:
            return (self.properties['titleShadowColor'])

class TextAttributes:
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties
        self.seperatorCount = None

    @property
    def fontStyle(self):
        if "fontStyle" in self.properties:
            return FontStyle(self.properties['fontStyle'])

    @property
    def tracking(self):
         if "tracking" in self.properties:
            return self.properties['tracking']

    @property
    def ligature(self):
         if "ligature" in self.properties:
            return self.properties['ligature']

    @property
    def lineSpacing(self):
        if "lineSpacing" in self.properties:
            return (self.properties['lineSpacing'])

class Button(View, FontStyle):
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def type(self):
        return "UIButton"

    @property
    def fontStyle(self):
        if "fontStyle" in self.properties:
            return FontStyle(self.properties['fontStyle'])

    @property
    def normalState(self):
        if "normalState" in self.properties:
            return NormalState(self.name, self.properties['normalState'])

    @property
    def selectedState(self):
        if "selectedState" in self.properties:
            return SelectedState(self.name, self.properties['selectedState'])

    @property
    def highlightedState(self):
        if "highlightedState" in self.properties:
            return HighlightedState(self.name, self.properties['highlightedState'])

class Label(View, FontStyle):
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def type(self):
        return "UILabel"

    @property
    def textColor(self):
        if "textColor" in self.properties:
            return (self.properties['textColor'])

    @property
    def textAlignment(self):
        if "textAlignment" in self.properties:
            return (self.properties['textAlignment'])

    @property
    def attributes(self):
        if "attributes" in self.properties:
            return TextAttributes(self.name, self.properties['attributes'])

class TextField(View):
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def type(self):
        return "UITextField"

    @property
    def textColor(self):
        if "textColor" in self.properties:
            return (self.properties['textColor'])

    @property
    def fontStyle(self):
        if "fontStyle" in self.properties:
            return FontStyle(self.properties['fontStyle'])

    @property
    def textAlignment(self):
        if "textAlignment" in self.properties:
            return (self.properties['textAlignment'])

    @property
    def backgroundColor(self):
        if "backgroundColor" in self.properties:
            return self.properties['backgroundColor']

    @property
    def borderStyle(self):
        if "borderStyle" in self.properties:
            return (self.properties['borderStyle'])

    @property
    def borderColor(self):
        if "borderColor" in self.properties:
            return (self.properties['borderColor'])

    @property
    def borderWidth(self):
        if "borderWidth" in self.properties:
            return (self.properties['borderWidth'])

    @property
    def cornerRadius(self):
        if "cornerRadius" in self.properties:
            return (self.properties['cornerRadius'])

class SegmentedControl(View):
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def type(self):
        return "UISegmentedControl"

    @property
    def fontStyle(self):
        if "fontStyle" in self.properties:
            return FontStyle(self.properties['fontStyle'])

    @property
    def normalState(self):
        if "normalState" in self.properties:
            return NormalState(self.name, self.properties['normalState'])

    @property
    def selectedState(self):
        if "selectedState" in self.properties:
            return SelectedState(self.name, self.properties['selectedState'])

    @property
    def highlightedState(self):
        if "highlightedState" in self.properties:
            return HighlightedState(self.name, self.properties['highlightedState'])

    @property
    def dividerColor(self):
        if "dividerColor" in self.properties:
            return (self.properties['dividerColor'])

class Font:
    def __init__(self, name):
        self.name = name

class HexColor:
    def __init__(self, hexValue, alpha):
        value = hexValue.lstrip('#')
        lv = len(value)
        rgbTuple = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        self.red = rgbTuple[0]
        self.green = rgbTuple[1]
        self.blue = rgbTuple[2]
        self.alpha = alpha

    def toSwiftRGBA(self):
        return "UIColor(red: %.1f/255.0, green: %.1f/255.0, blue: %.1f/255.0, alpha: %.1f)" % (self.red, self.green, self.blue, self.alpha)

class RGBColor:
    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def toSwiftRGBA(self):
        return "UIColor(red: %.1f/255.0, green: %.1f/255.0, blue: %.1f/255.0, alpha: %.1f)" % (self.red, self.green, self.blue, self.alpha)