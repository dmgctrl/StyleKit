class Label:
    def __init__(self, name):
        self.name = name
        self.textColor = None
        self.font = None
        self.fontSize = None

    def setTextColor(self, textColor):
        self.textColor = textColor

class Button:
    def __init__(self, name):
        self.name = name
        self.state = None
        self.backgroundColor = None
        self.titleColor = None
        self.titleShadowColor = None
        self.titleForState = None
        self.titleColorForState = None
        self.titleShadowColorForState = None
        self.cornerRadius = None
        self.borderColor = None
        self.borderWidth = None
        self.backgroundImageForState = None
        self.imageForState = None
        self.reversesTitleShadowWhenHighlighted = None

    def setBackgroundColor(self, backgroundColor):
        self.backgroundColor = backgroundColor

    def setTitleColor(self, titleColor):
        self.titleColor = titleColor

    def setTitleShadowColor(self, titleShadowColor):
        self.titleShadowColor = titleShadowColor

    def setTitleForState(self, titleForState, state):
        self.titleForState = titleForState
        self.state = state

    def setTitleColorForState(self, titleColorForState, state):
        self.titleColorForState = titleColorForState
        self.state = state

    def titleShadowColorForState(self, titleShadowColorForState, state):
        self.titleShadowColorForState = titleShadowColorForState
        self.state = state

    def setCornerRadius(self, cornerRadius):
        self.cornerRadius = cornerRadius

    def setBorderColor(self, borderColor):
        self.borderColor = borderColor

    def setBorderWidth(self, borderWidth):
        self.borderWidth = borderWidth

    def setBackgroundImageForState(self, backgroundImageForState, state):
        self.backgroundImageForState = backgroundImageForState
        self.state = state

    def setImageForState(self, imageForState, state):
        self.imageForState = imageForState
        self.state = state

    def setReversesTitleShadowWhenHighlighted(self,reversesTitleShadowWhenHighlighted = bool ):
        self.reversesTitleShadowWhenHighlighted = reversesTitleShadowWhenHighlighted

class Image:
    def __init__(self, name, filename):
        self.name = name
        self.filename = filename

    def toSwift(self):
        return "UIImage (named: %s)" % (self.filename)

class Font:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def toSwift(self):
        return "UIFont (name: %s, size: %s)" % (self.name, self.size)

class Color:
    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def toSwiftRGBA(self):
        return "UIColor(red: %.2f, green: %.2f, blue: %.2f, alpha: %.2f)" % (self.red, self.green, self.blue, self.alpha)

    def rgb_to_hex(self, r,g,b):
        return "#%02X%02X%02X" % (r,g,b)