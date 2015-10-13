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
        self.backgroundColor = None
        self.titleColor = None

    def setBackgroundColor(self, backgroundColor):
        self.backgroundColor = backgroundColor

    def setTitleColor(self, titleColor):
        self.titleColor = titleColor

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

