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
        return "UIFont (name: %s, size: %s)" % (self.font, self.size)

class Normal:
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def titleColorNormal(self):
        if "titleColor" in self.properties:
            return (self.properties['titleColor'])

    @property
    def state(self):
        return ".Normal"

class Highlighted:
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def titleColorHighlighted(self):
        if "titleColor" in self.properties:
            return (self.properties['titleColor'])

class Selected:
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def titleColorSelected(self):
        if "titleColor" in self.properties:
            return (self.properties['titleColor'])

    @property
    def state(self):
        return ".Selected"

class Attributes:
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties
        self.seperatorCount = None

    @property
    def font(self):
        if "font" in self.properties:
            return Font(self.properties['fontStyle'])

    @property
    def foregroundColor(self):
        if "foregroundColor" in self.properties:
            return self.properties['foregroundColor']

    @property
    def backgroundColor(self):
        if "backgroundColor" in self.properties:
            return self.properties['backgroundColor']

    @property
    def kerning(self):
         if "kerning" in self.properties:
            return self.properties['kerning']

    @property
    def ligature(self):
         if "ligature" in self.properties:
            return self.properties['ligature']

class Button(View, Attributes, Normal, Selected, Highlighted, FontStyle):
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def normal(self):
        if "normal" in self.properties:
            return Normal(self.name, self.properties['normal'])

    @property
    def selected(self):
        if "selected" in self.properties:
            return Selected(self.name, self.properties['selected'])

    @property
    def highlighted(self):
        if "highlighted" in self.properties:
            return Highlighted(self.name, self.properties['highlighted'])

    @property
    def attributes(self):
        if "attributes" in self.properties:
            return Attributes(self.name, self.properties['attributes'])

    @property
    def titleShadowColor(self):
        if "titleShadowColor" in self.properties:
            return (self.properties['titleShadowColor'])

    @property
    def backgroundImage(self):
        if "backgroundimage" in self.properties:
            return (self.properties['backgroundimage'])

    @property
    def fontStyle(self):
        if "fontStyle" in self.properties:
            return FontStyle(self.properties['fontStyle'])

    @property
    def type(self):
        return "UIButton"


class Label(View, Attributes, FontStyle):
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def attributes(self):
        if "attributes" in self.properties:
            return Attributes(self.name, self.properties['attributes'])

    @property
    def textColor(self):
        if "textColor" in self.properties:
            return (self.properties['textColor'])

    @property
    def type(self):
        return "UILabel"

    @property
    def textAlignment(self):
        if "textAlignment" in self.properties:
            return (self.properties['textAlignment'])

    @property
    def fontStyle(self):
        if "fontStyle" in self.properties:
            return FontStyle(self.properties['fontStyle'])

class TextField(View, Attributes):
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def attributes(self):
        if "attributes" in self.properties:
            return Attributes(self.name, self.properties['attributes'])

    @property
    def textColor(self):
        if "textColor" in self.properties:
            return (self.properties['textColor'])

    @property
    def type(self):
        return "UITextField"

    @property
    def fontStyle(self):
        if "fontStyle" in self.properties:
            return FontStyle(self.properties['fontStyle'])

    @property
    def textAlignment(self):
        if "textAlignment" in self.properties:
            return (self.properties['textAlignment'])

    @property
    def borderStyle(self):
        if "borderStyle" in self.properties:
            return (self.properties['borderStyle'])

class SegmentedControl(View, Attributes):
    def __init__(self, name, properties = {}):
        self.name = name
        self.properties = properties

    @property
    def normalColor(self):
        if "textColor" in self.properties:
            return (self.properties['normalColor'])

    @property
    def selectedColor(self):
        if "textColor" in self.properties:
            return (self.properties['selectedColor'])

    @property
    def dividerColor(self):
        if "textColor" in self.properties:
            return (self.properties['dividerColor'])

    @property
    def attributes(self):
        if "attributes" in self.properties:
            return Attributes(self.name, self.properties['attributes'])

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