import UIKit

class Style: NSObject {
    
    static let sharedInstance = Style()
    
    var fonts = [String: String]()
    var colors = [String: UIColor]()
    var imageNames: [String: String]? = nil
    var labelStyles = [String: [String:AnyObject]]()
    var buttonStyles = [String: [String:AnyObject]]()
    var textFieldStyles = [String: [String:AnyObject]]()
    
    override init() {
        super.init()
        serialize()
    }
    
    
    @IBOutlet var StyleLabel: [UILabel]! {
        didSet {
            var info = [String: UILabel]()
            for label in StyleLabel {
                if let styleTag = label.styleTag {
                    info[styleTag] = label
                }
            }
            self.style(withLabelsAndStyles: info)
        }
    }
    
    @IBOutlet var StyleButton: [UIButton]! {
        didSet {
            var info = [String: UIButton]()
            for button in StyleButton {
                if let styleTag = button.styleTag {
                    info[styleTag] = button
                }
            }
            self.style(withButtonsAndStyles: info)
        }
    }
    
    @IBOutlet var StyleTextField: [UITextField]! {
        didSet {
            var info = [String: UITextField]()
            for textField in StyleTextField {
                if let styleTag = textField.styleTag {
                    info[styleTag] = textField
                }
            }
            self.style(withTextFieldsAndStyles: info)
        }
    }
    
    //Mark: Serialize
    
    func configurationStyleURL() -> NSURL? {
        let documentsDirPath = urlForFileInDocumentsDirectory("Style.json")
        if NSFileManager.defaultManager().fileExistsAtPath(documentsDirPath.path!)   {
            return documentsDirPath
        }

        let bundlePath = NSBundle.mainBundle().pathForResource("Style", ofType: "json")
        return NSURL(fileURLWithPath: bundlePath!)
    }
    
    func urlForFileInDocumentsDirectory(fileName: String) -> NSURL {
        let docsDir = NSFileManager.defaultManager().URLsForDirectory(.DocumentDirectory, inDomains: .UserDomainMask)[0]
        return docsDir.URLByAppendingPathComponent(fileName)
    }
    
    func serialize() {
        
        let stylePath = configurationStyleURL()!
        
        do {
            
            let data = try NSData(contentsOfURL: stylePath, options: NSDataReadingOptions.DataReadingMappedIfSafe)
            let json = try NSJSONSerialization.JSONObjectWithData(data, options: .AllowFragments)
            
            if let items = json["Fonts"] as? [String: String] {
                fonts = items
            }
            
            if let colorDict = json["Colors"] as? [String: [String: Int]] {
                for (colorKey, components) in colorDict {
                    if let red = components["red"],
                        let green = components["green"],
                        let blue = components["blue"],
                        let alpha = components["alpha"] {
                            colors[colorKey] = UIColor(red: CGFloat(red)/255, green: CGFloat(green)/255, blue: CGFloat(blue)/255, alpha: CGFloat(alpha))
                    }
                }
            }
            
            imageNames = json["Images"] as? [String: String]
            
            if let labelDict = json["Labels"] as? [String: [String:AnyObject]] {
                for (labelKey, specification) in labelDict {
                    labelStyles[labelKey] = serializeLabelSpec(specification)
                }
            }
            
            if let buttonDict = json["Buttons"] as? [String: [String:AnyObject]] {
                for (buttonKey, specification) in buttonDict {
                    buttonStyles[buttonKey] = serializeButtonSpec(specification)
                }
            }
            
            if let textFieldDict = json["TextFields"] as? [String: [String:AnyObject]] {
                for (textFieldKey, specification) in textFieldDict {
                    textFieldStyles[textFieldKey] = serializeTextFieldSpec(specification)
                }
            }
            
        } catch {
            assert(false,"error serializing JSON: \(error)")
        }
    }
    
    class FontStyle {
        var fontName: String
        var size: Int
        init(fontName:String, size:Int)  {
            self.size = size
            self.fontName = fontName
        }
    }
    
    func serializeButtonSpec(spec: [String:AnyObject]) -> [String:AnyObject] {
        var result = [String:AnyObject]()
        for (key,value) in spec {
            switch key {
            case "fontStyle":
                if let nameKey = value["font"] as? String,
                    font = fonts[nameKey],
                    size = value["size"] as? Int {
                        result[key] = FontStyle(fontName: font, size: size)
                } else {
                    assert(false)
                }
            case "borderWidth":
                result[key] = spec[key]
            case "borderColor":
                if let colorKey = value as? String, color = colors[colorKey]  {
                    result[key] = color
                } else {
                    assert(false)
                }
            case "cornerRadius":
                result[key] = spec[key]
            case "normal":
                if let colorKey = value["titleColor"] as? String, color = colors[colorKey]  {
                    result[key] = color
                } else {
                    assert(false)
                }
            default:
                assert(false, "\(key) not Supported")
            }
        }
        return result
    }
    
    func serializeTextFieldSpec(spec: [String:AnyObject]) -> [String:AnyObject] {
        var result = [String:AnyObject]()
        for (key,value) in spec {
            switch key {
            case "fontStyle":
                if let nameKey = value["font"] as? String,
                    font = fonts[nameKey],
                    size = value["size"] as? Int {
                        result[key] = FontStyle(fontName: font, size: size)
                } else {
                    assert(false, "invalid option for key: \(key)")
                }
            case "borderWidth":
                result[key] = spec[key]
            case "textColor":
                if let colorKey = value as? String, color = colors[colorKey]  {
                    result[key] = color
                } else {
                    assert(false, "invalid option for key: \(key)")
                }
            case "borderColor":
                if let colorKey = value as? String, color = colors[colorKey]  {
                    result[key] = color
                } else {
                    assert(false, "invalid option for key: \(key)")
                }
            case "textAlignment":
                let allowedValues = ["Left","Center","Right","Justified","Natural"]
                if allowedValues.contains(value as! String) {
                    result[key] = allowedValues.indexOf(value as! String)
                } else {
                    assert(false, "invalid option for key: \(key)")
                }
            case "borderStyle":
                let allowedValues = ["None","Line","Bezel","RoundedRect"]
                if allowedValues.contains(value as! String) {
                    result[key] = allowedValues.indexOf(value as! String)
                } else {
                    assert(false, "invalid option for key: \(key)")
                }
            case "cornerRadius":
                result[key] = spec[key]
            default:
                assert(false, "\(key) not Supported")
            }
        }
        return result
    }
    
    func serializeLabelSpec(spec: [String:AnyObject]) -> [String:AnyObject] {
        var result = [String:AnyObject]()
        for (key,value) in spec {
            switch key {
            case "fontStyle":
                if let nameKey = value["font"] as? String,
                    font = fonts[nameKey],
                    size = value["size"] as? Int {
                        result[key] = FontStyle(fontName: font, size: size)
                } else {
                    assert(false)
                }
            default:
                assert(false, "\(key) not Supported")
            }
        }
        return result
    }
    
    //MARK: Apply Styles
    
    func style(withLabelsAndStyles labelInfo: [String: UILabel]?) {
        guard let info = labelInfo else {
            return
        }
        
        for (styleKey, element) in info {
            guard let styles = labelStyles[styleKey] else {
                return
            }
            
            for (property, value) in styles {
                switch property {
                case LabelProperties.FontStyle:
                    if let fontStyle = value as? FontStyle {
                        element.font = UIFont(name: fontStyle.fontName, size: CGFloat(fontStyle.size))
                    }
                default:
                    return
                }
            }
        }
    }
    
    func style(withButtonsAndStyles buttonInfo: [String: UIButton]?) {
        guard let info = buttonInfo else {
            return
        }
        
        for (styleKey, element) in info {
            guard let styles = buttonStyles[styleKey] else {
                return
            }
            
            for (property, value) in styles {
                switch property {
                case ButtonProperties.FontStyle:
                    if let fontStyle = value as? FontStyle {
                        element.titleLabel?.font = UIFont(name: fontStyle.fontName, size: CGFloat(fontStyle.size))
                    }
                case ButtonProperties.BorderWidth:
                    if let borderWidth = value as? Int {
                        element.layer.borderWidth = CGFloat(borderWidth)
                    }
                case ButtonProperties.BorderColor:
                    if let borderColor = value as? UIColor {
                        element.layer.borderColor = borderColor.CGColor
                    }
                case ButtonProperties.CornerRadius:
                    if let cornerRadius = value as? Int {
                        element.layer.cornerRadius = CGFloat(cornerRadius)
                    }
                case ButtonProperties.Normal:
                    if let color = value as? UIColor {
                        element.setTitleColor(color, forState: .Normal)
                    }
                default:
                    return
                }
            }
        }
    }
    
    func style(withTextFieldsAndStyles textFieldInfo: [String: UITextField]?) {
        guard let info = textFieldInfo else {
            return
        }
        
        for (styleKey, element) in info {
            guard let styles = textFieldStyles[styleKey] else {
                return
            }
            
            for (property, value) in styles {
                switch property {
                case TextFieldProperties.FontStyle:
                    if let fontStyle = value as? FontStyle {
                        element.font = UIFont(name: fontStyle.fontName, size: CGFloat(fontStyle.size))
                    }
                case TextFieldProperties.BorderWidth:
                    if let borderWidth = value as? Int {
                        element.layer.borderWidth = CGFloat(borderWidth)
                    }
                case TextFieldProperties.BorderColor:
                    if let borderColor = value as? UIColor {
                        element.layer.borderColor = borderColor.CGColor
                    }
                case TextFieldProperties.TextAlignment:
                    if let aValue = value as? Int {
                        guard let textAlignment = NSTextAlignment(rawValue: aValue) else {
                            break
                        }
                        element.textAlignment = textAlignment
                    }
                case TextFieldProperties.BorderStyle:
                    if let aValue = value as? Int {
                        guard let textBorderStyle = UITextBorderStyle(rawValue: aValue) else {
                            break
                        }
                        element.borderStyle = textBorderStyle
                    }
                case TextFieldProperties.CornerRadius:
                    if let cornerRadius = value as? Int {
                        element.layer.cornerRadius = CGFloat(cornerRadius)
                    }
                case TextFieldProperties.TextColor:
                    element.textColor = value as? UIColor
                default:
                    return
                }
            }
        }
    }
}
