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
    var sliderStyles = [String: [String: AnyObject]]()
    var stepperStyles: [String: [String: AnyObject]]?
    
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
                    if let spec = serializeButtonSpec(specification) {
                        buttonStyles[buttonKey] = spec
                    }
                }
            }
            
            if let textFieldDict = json[UIElements.TextFields.rawValue] as? [String: [String:AnyObject]] {
                for (textFieldKey, specification) in textFieldDict {
                    if let spec = serializeTextFieldSpec(specification) {
                        textFieldStyles[textFieldKey] = spec
                    }
                }
            }
            
            if let segmentedControlDict = json[UIElements.SegmentedControls.rawValue] as? [String: [String: AnyObject]] {
                for (segmentedControlKey, specification) in segmentedControlDict {
                    segmentedControlStyles[segmentedControlKey] = specification
                }
            }
            
            if let sliderDict = json[UIElements.Sliders.rawValue] as? [String: [String: AnyObject]] {
                for (sliderKey, specification) in sliderDict {
                    sliderStyles[sliderKey] = specification
                }
            }
            
            if let stepperDict = json[UIElements.Steppers.rawValue] as? [String: [String: AnyObject]] {
                stepperStyles = [String: [String: AnyObject]]()
                
                guard var theStepperStyles = stepperStyles else {
                    return
                }
                
                for (stepperKey, specification) in stepperDict {
                    theStepperStyles[stepperKey] = specification
                }
                
                stepperStyles = theStepperStyles
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
    
    func serializeButtonSpec(spec: [String:AnyObject]) -> [String:AnyObject]? {
        var result = [String:AnyObject]()
        for (key,value) in spec {
            guard let theKey = ButtonProperties(rawValue: key) else {
                return nil
            }
            
            switch theKey {
                case ButtonProperties.FontStyle:
                    if let nameKey = value[FontProperties.Name.rawValue] as? String,
                        font = fonts[nameKey],
                        size = value[FontProperties.Size.rawValue] as? Int {
                            result[key] = FontStyle(fontName: font, size: size)
                    } else {
                        assert(false)
                    }
                case ButtonProperties.BorderWidth:
                    result[key] = spec[key]
                case ButtonProperties.BorderColor:
                    if let colorKey = value as? String, color = colors[colorKey]  {
                        result[key] = color
                    } else {
                        assert(false)
                    }
                case ButtonProperties.CornerRadius:
                    result[key] = spec[key]
                case ButtonProperties.Normal:
                    if let colorKey = value[CommonProperties.TitleColor.rawValue] as? String, color = colors[colorKey]  {
                        result[key] = color
                    } else {
                        assert(false)
                    }
            }
        }
        return result
    }
    
    func serializeTextFieldSpec(spec: [String:AnyObject]) -> [String:AnyObject]? {
        var result = [String:AnyObject]()
        for (key,value) in spec {
            guard let theKey = TextFieldProperties(rawValue: key) else {
                return nil
            }
            
            switch theKey {
                case TextFieldProperties.FontStyle:
                    if let nameKey = value[FontProperties.Name.rawValue] as? String,
                        font = fonts[nameKey],
                        size = value[FontProperties.Size.rawValue] as? Int {
                            result[key] = FontStyle(fontName: font, size: size)
                    } else {
                        assert(false, "invalid option for key: \(key)")
                    }
                case TextFieldProperties.BorderWidth:
                    result[key] = spec[key]
                case TextFieldProperties.TextColor:
                    if let colorKey = value as? String, color = colors[colorKey]  {
                        result[key] = color
                    } else {
                        assert(false, "invalid option for key: \(key)")
                    }
                case TextFieldProperties.BorderColor:
                    if let colorKey = value as? String, color = colors[colorKey]  {
                        result[key] = color
                    } else {
                        assert(false, "invalid option for key: \(key)")
                    }
                case TextFieldProperties.TextAlignment:
                    let allowedValues = ["Left","Center","Right","Justified","Natural"]
                    if allowedValues.contains(value as! String) {
                        result[key] = allowedValues.indexOf(value as! String)
                    } else {
                        assert(false, "invalid option for key: \(key)")
                    }
                case TextFieldProperties.BorderStyle:
                    let allowedValues = ["None","Line","Bezel","RoundedRect"]
                    if allowedValues.contains(value as! String) {
                        result[key] = allowedValues.indexOf(value as! String)
                    } else {
                        assert(false, "invalid option for key: \(key)")
                    }
                case TextFieldProperties.CornerRadius:
                    result[key] = spec[key]
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
                guard let theProperty = LabelProperties(rawValue: property) else {
                    return
                }
                
                switch theProperty {
                    case LabelProperties.FontStyle:
                        if let fontStyle = value as? FontStyle {
                            element.font = UIFont(name: fontStyle.fontName, size: CGFloat(fontStyle.size))
                        }
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
                guard let theProperty = ButtonProperties(rawValue: property) else {
                    return
                }
                
                switch theProperty {
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
                guard let theProperty = TextFieldProperties(rawValue: property) else {
                    return
                }
                
                switch theProperty {
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
                guard let theProperty = SegmentedControlProperties(rawValue: property) else {
                    return
                }
                
                switch theProperty {
                    case SegmentedControlProperties.FontStyle:
                        guard let fontInfo = value as? [String: AnyObject], fontKey = fontInfo[FontProperties.Name.rawValue] as? String,
                            fontSize = fontInfo[FontProperties.Size.rawValue] as? Int else {
                            break
                        }
                        guard let fontName = fonts[fontKey], font = UIFont(name: fontName, size: CGFloat(fontSize)) else {
                            break
                        }
                        normalAttributes[NSFontAttributeName] = font
                        selectedAttributes[NSFontAttributeName] = font
                        
                    case SegmentedControlProperties.NormalState:
                        if let textColorInfo = value as? [String: String], textColorKey = textColorInfo[CommonProperties.TextColor.rawValue],
                            color = colors[textColorKey] {
                            normalAttributes[NSForegroundColorAttributeName] = color
                        }
                        
                    case SegmentedControlProperties.SelectedState:
                        if let textColorInfo = value as? [String: String], textColorKey = textColorInfo[CommonProperties.TextColor.rawValue],
                            color = colors[textColorKey] {
                            selectedAttributes[NSForegroundColorAttributeName] = color
                        }
                    
                    case SegmentedControlProperties.TintColor:
                        if let tintColorKey = value as? String, tintColor = colors[tintColorKey] {
                            element.tintColor = tintColor
                        }
                }
                
                element.setTitleTextAttributes(normalAttributes, forState: .Normal)
                element.setTitleTextAttributes(selectedAttributes, forState: .Selected)
            }
        }
    }
    
    func style(withSlidersAndStyles sliderInfo: [String: UISlider]?) {
        guard let info = sliderInfo else {
            return
        }
        
        for (styleKey, element) in info {
            guard let styles = sliderStyles[styleKey] else {
                return
            }
            
            guard let theImageNames = imageNames else {
                return
            }
            
            for (property, value) in styles {
                guard let theProperty = SliderProperties(rawValue: property) else {
                    return
                }
                
                switch theProperty {
                    case .MaximumTrackTintColor:
                        if let colorKey = value as? String, color = colors[colorKey] {
                            element.maximumTrackTintColor = color
                        }
                    case .MinimumTrackTintColor:
                        if let colorKey = value as? String, color = colors[colorKey] {
                            element.minimumTrackTintColor = color
                        }
                    case .ThumbImage:
                        if let imageKey = value as? String, theImageNames = imageNames, imageName = theImageNames[imageKey] {
                            element.setThumbImage(UIImage(named: imageName), forState: .Normal)
                        }
                    case .MinimumTrackImage:
                        if let imageKey = value as? String, imageName = theImageNames[imageKey] {
                            element.setMinimumTrackImage(UIImage(named: imageName), forState: .Normal)
                        }
                    case .MaximumTrackImage:
                        if let imageKey = value as? String, imageName = theImageNames[imageKey] {
                            element.setMaximumTrackImage(UIImage(named: imageName), forState: .Normal)
                        }
                }
            }
        }
        
    }
    
    func style(withSteppersAndStyles stepperInfo: [String: UIStepper]?) {
        guard let info = stepperInfo else {
            return
        }
        
        for (styleKey, element) in info {
            guard let theStepperStyles = stepperStyles, styles = theStepperStyles[styleKey], theImageNames = imageNames else {
                return
            }
            
            for (property, value) in styles {
                guard let theProperty = StepperProperties(rawValue: property) else {
                    return
                }
                
                switch theProperty {
                    case .TintColor:
                        if let colorKey = value as? String, color = colors[colorKey] {
                            element.tintColor = color
                        }
                    case .IncrementImage:
                        if let imageKey = value as? String, imageName = theImageNames[imageKey] {
                            element.setIncrementImage(UIImage(named: imageName), forState: .Normal)
                        }
                    case .DecrementImage:
                        if let imageKey = value as? String, imageName = theImageNames[imageKey] {
                            element.setDecrementImage(UIImage(named: imageName), forState: .Normal)
                        }
                    case .BackgroundImage:
                        if let imageKey = value as? String, imageName = theImageNames[imageKey] {
                            element.setBackgroundImage(UIImage(named: imageName), forState: .Normal)
                        }
                }
            }
        }
    }
    
}
