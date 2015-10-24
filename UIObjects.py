class uiObject:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.textColor = None
        self.font = None
        self.backgroundColor = None
        self.titleColor = None
        self.titleLabel = None
        self.cornerRadius = None
        self.borderColor = None
        self.borderWidth = None
        self.titleShadowColor = None
        self.backgroundImage = None

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

    def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))