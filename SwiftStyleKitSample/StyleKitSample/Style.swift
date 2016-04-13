import UIKit

class Style: NSObject {
    
    static let sharedInstance = Style()
    
    var fonts = [String: String]()
    var colors = [String: UIColor]()
    var imageNames: [String: String]? = nil
    var labelStyles = [String: [String:AnyObject]]()
    var buttonStyles = [String: [String:AnyObject]]()
    var textFieldStyles = [String: [String:AnyObject]]()
    var segmentedControlStyles = [String: [String: AnyObject]]()
    
    override init() {
        super.init()
        serialize()
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
            
            if let items = json[CommonObjects.Fonts.rawValue] as? [String: String] {
                fonts = items
            }
            
            if let colorDict = json[CommonObjects.Colors.rawValue] as? [String: [String: Int]] {
                for (colorKey, components) in colorDict {
                    if let red = components[ColorProperties.Red.rawValue],
                        let green = components[ColorProperties.Green.rawValue],
                        let blue = components[ColorProperties.Blue.rawValue],
                        let alpha = components[ColorProperties.Alpha.rawValue] {
                            colors[colorKey] = UIColor(red: CGFloat(red)/255, green: CGFloat(green)/255, blue: CGFloat(blue)/255, alpha: CGFloat(alpha))
                    }
                }
            }
            
            imageNames = json[CommonObjects.Images.rawValue] as? [String: String]
            
            if let labelDict = json[UIElements.Labels.rawValue] as? [String: [String:AnyObject]] {
                for (labelKey, specification) in labelDict {
                    labelStyles[labelKey] = serializeLabelSpec(specification)
                }
            }
            
            if let buttonDict = json[UIElements.Buttons.rawValue] as? [String: [String:AnyObject]] {
                for (buttonKey, specification) in buttonDict {
                    buttonStyles[buttonKey] = serializeButtonSpec(specification)
                }
            }
            
            if let textFieldDict = json[UIElements.TextFields.rawValue] as? [String: [String:AnyObject]] {
                for (textFieldKey, specification) in textFieldDict {
                    textFieldStyles[textFieldKey] = serializeTextFieldSpec(specification)
                }
            }
            
            if let segmentedControlDict = json[UIElements.SegmentedControls.rawValue] as? [String: [String: AnyObject]] {
                for (segmentedControlKey, specification) in segmentedControlDict {
                    segmentedControlStyles[segmentedControlKey] = specification
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
            case ButtonProperties.FontStyle.rawValue:
                if let nameKey = value[FontProperties.Name.rawValue] as? String,
                    font = fonts[nameKey],
                    size = value[FontProperties.Size.rawValue] as? Int {
                        result[key] = FontStyle(fontName: font, size: size)
                } else {
                    assert(false)
                }
            case ButtonProperties.BorderWidth.rawValue:
                result[key] = spec[key]
            case ButtonProperties.BorderColor.rawValue:
                if let colorKey = value as? String, color = colors[colorKey]  {
                    result[key] = color
                } else {
                    assert(false)
                }
            case ButtonProperties.CornerRadius.rawValue:
                result[key] = spec[key]
            case ButtonProperties.Normal.rawValue:
                if let colorKey = value[CommonProperties.TitleColor.rawValue] as? String, color = colors[colorKey]  {
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
            case TextFieldProperties.FontStyle.rawValue:
                if let nameKey = value[FontProperties.Name.rawValue] as? String,
                    font = fonts[nameKey],
                    size = value[FontProperties.Size.rawValue] as? Int {
                        result[key] = FontStyle(fontName: font, size: size)
                } else {
                    assert(false, "invalid option for key: \(key)")
                }
            case TextFieldProperties.BorderWidth.rawValue:
                result[key] = spec[key]
            case TextFieldProperties.TextColor.rawValue:
                if let colorKey = value as? String, color = colors[colorKey]  {
                    result[key] = color
                } else {
                    assert(false, "invalid option for key: \(key)")
                }
            case TextFieldProperties.BorderColor.rawValue:
                if let colorKey = value as? String, color = colors[colorKey]  {
                    result[key] = color
                } else {
                    assert(false, "invalid option for key: \(key)")
                }
            case TextFieldProperties.TextAlignment.rawValue:
                let allowedValues = ["Left","Center","Right","Justified","Natural"]
                if allowedValues.contains(value as! String) {
                    result[key] = allowedValues.indexOf(value as! String)
                } else {
                    assert(false, "invalid option for key: \(key)")
                }
            case TextFieldProperties.BorderStyle.rawValue:
                let allowedValues = ["None","Line","Bezel","RoundedRect"]
                if allowedValues.contains(value as! String) {
                    result[key] = allowedValues.indexOf(value as! String)
                } else {
                    assert(false, "invalid option for key: \(key)")
                }
            case TextFieldProperties.CornerRadius.rawValue:
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
            case LabelProperties.FontStyle.rawValue:
                if let nameKey = value[FontProperties.Name.rawValue] as? String,
                    font = fonts[nameKey],
                    size = value[FontProperties.Size.rawValue] as? Int {
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
                case LabelProperties.FontStyle.rawValue:
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
                case ButtonProperties.FontStyle.rawValue:
                    if let fontStyle = value as? FontStyle {
                        element.titleLabel?.font = UIFont(name: fontStyle.fontName, size: CGFloat(fontStyle.size))
                    }
                case ButtonProperties.BorderWidth.rawValue:
                    if let borderWidth = value as? Int {
                        element.layer.borderWidth = CGFloat(borderWidth)
                    }
                case ButtonProperties.BorderColor.rawValue:
                    if let borderColor = value as? UIColor {
                        element.layer.borderColor = borderColor.CGColor
                    }
                case ButtonProperties.CornerRadius.rawValue:
                    if let cornerRadius = value as? Int {
                        element.layer.cornerRadius = CGFloat(cornerRadius)
                    }
                case ButtonProperties.Normal.rawValue:
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
                case TextFieldProperties.FontStyle.rawValue:
                    if let fontStyle = value as? FontStyle {
                        element.font = UIFont(name: fontStyle.fontName, size: CGFloat(fontStyle.size))
                    }
                case TextFieldProperties.BorderWidth.rawValue:
                    if let borderWidth = value as? Int {
                        element.layer.borderWidth = CGFloat(borderWidth)
                    }
                case TextFieldProperties.BorderColor.rawValue:
                    if let borderColor = value as? UIColor {
                        element.layer.borderColor = borderColor.CGColor
                    }
                case TextFieldProperties.TextAlignment.rawValue:
                    if let aValue = value as? Int {
                        guard let textAlignment = NSTextAlignment(rawValue: aValue) else {
                            break
                        }
                        element.textAlignment = textAlignment
                    }
                case TextFieldProperties.BorderStyle.rawValue:
                    if let aValue = value as? Int {
                        guard let textBorderStyle = UITextBorderStyle(rawValue: aValue) else {
                            break
                        }
                        element.borderStyle = textBorderStyle
                    }
                case TextFieldProperties.CornerRadius.rawValue:
                    if let cornerRadius = value as? Int {
                        element.layer.cornerRadius = CGFloat(cornerRadius)
                    }
                case TextFieldProperties.TextColor.rawValue:
                    element.textColor = value as? UIColor
                default:
                    return
                }
            }
        }
    }
    
    func style(withSegmentedControlsAndStyles segmentedControlInfo: [String: UISegmentedControl]?) {
        guard let info = segmentedControlInfo else {
            return
        }
        
        for (styleKey, element) in info {
            guard let styles = segmentedControlStyles[styleKey] else {
                return
            }
            
            var normalAttributes = [String: AnyObject]()
            var selectedAttributes = [String: AnyObject]()
            
            for (property, value) in styles {
                
                switch property {
                    case SegmentedControlProperties.FontStyle.rawValue:
                        guard let fontInfo = value as? [String: AnyObject], fontKey = fontInfo[FontProperties.Name.rawValue] as? String,
                            fontSize = fontInfo[FontProperties.Size.rawValue] as? Int else {
                            break
                        }
                        guard let fontName = fonts[fontKey], font = UIFont(name: fontName, size: CGFloat(fontSize)) else {
                            break
                        }
                        normalAttributes[NSFontAttributeName] = font
                        selectedAttributes[NSFontAttributeName] = font
                        break
                        
                    case SegmentedControlProperties.NormalState.rawValue:
                        if let textColorInfo = value as? [String: String], textColorKey = textColorInfo[CommonProperties.TextColor.rawValue],
                            color = colors[textColorKey] {
                            normalAttributes[NSForegroundColorAttributeName] = color
                        }
                        break
                        
                    case SegmentedControlProperties.SelectedState.rawValue:
                        if let textColorInfo = value as? [String: String], textColorKey = textColorInfo[CommonProperties.TextColor.rawValue],
                            color = colors[textColorKey] {
                            selectedAttributes[NSForegroundColorAttributeName] = color
                        }
                        break
                    
                case SegmentedControlProperties.TintColor.rawValue:
                    if let tintColorKey = value as? String, tintColor = colors[tintColorKey] {
                        element.tintColor = tintColor
                    }
                    break
                    
                    default:
                        return
                }
                
                element.setTitleTextAttributes(normalAttributes, forState: .Normal)
                element.setTitleTextAttributes(selectedAttributes, forState: .Selected)
            }
        }
    }
    
}
