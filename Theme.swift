import UIKit

class Theme: NSObject {

    static let sharedInstance = Theme()    
    
    let primaryFontMedium: String = "BrandonGrotesque-Medium"    
    let primaryFontBlack: String = "BrandonGrotesque-Black"    
    let primaryFontLight: String = "BrandonGrotesque-Light"    
    let primaryFontLightItalic: String = "BrandonGrotesque-LightItalic"    
    let primaryFontBold: String = "BrandonGrotesque-Bold"    
    
    let baseColorRedLight = UIColor(red: 250.0/255.0, green: 110.0/255.0, blue: 92.0/255.0, alpha: 1.0)    
    let baseBlackColor = UIColor(red: 0.0/255.0, green: 0.0/255.0, blue: 0.0/255.0, alpha: 0.5)    
    let baseColorGreyLight = UIColor(red: 194.0/255.0, green: 194.0/255.0, blue: 194.0/255.0, alpha: 1.0)    
    let baseClearColor = UIColor(red: 0.0/255.0, green: 0.0/255.0, blue: 0.0/255.0, alpha: 0.0)    
    let baseColorBlueMedium = UIColor(red: 77.0/255.0, green: 191.0/255.0, blue: 213.0/255.0, alpha: 1.0)    
    let baseColorWhite = UIColor(red: 255.0/255.0, green: 255.0/255.0, blue: 255.0/255.0, alpha: 1.0)    
    let activitySecondaryColor = UIColor(red: 219.0/255.0, green: 96.0/255.0, blue: 85.0/255.0, alpha: 1.0)    
    let baseColorRedDark = UIColor(red: 197.0/255.0, green: 35.0/255.0, blue: 38.0/255.0, alpha: 1.0)    
    let baseColorGreyDark = UIColor(red: 102.0/255.0, green: 102.0/255.0, blue: 102.0/255.0, alpha: 1.0)    
    let activityPrimaryColor = UIColor(red: 242.0/255.0, green: 114.0/255.0, blue: 101.0/255.0, alpha: 1.0)    
    let baseColorRedMedium = UIColor(red: 234.0/255.0, green: 75.0/255.0, blue: 44.0/255.0, alpha: 1.0)    
    let baseColorGreyMedium = UIColor(red: 135.0/255.0, green: 135.0/255.0, blue: 135.0/255.0, alpha: 1.0)    
    let baseColorBlueDark = UIColor(red: 65.0/255.0, green: 162.0/255.0, blue: 182.0/255.0, alpha: 1.0)    
    let activityTertiaryColor = UIColor(red: 185.0/255.0, green: 80.0/255.0, blue: 71.0/255.0, alpha: 1.0)    
    let baseColorBlueLight = UIColor(red: 73.0/255.0, green: 208.0/255.0, blue: 223.0/255.0, alpha: 1.0)    
    let baseColorGreyVeryLight = UIColor(red: 62.0/255.0, green: 62.0/255.0, blue: 62.0/255.0, alpha: 1.0)    
    
    let buttonImage1 = UIImage(named: "black_button_image")    
    
    @IBOutlet var P2Label: [UILabel]! {        
        didSet {            
            styleP2Label(P2Label)            
        }        
    }    
    
    @IBOutlet var P1Label: [UILabel]! {        
        didSet {            
            styleP1Label(P1Label)            
        }        
    }    
    
    @IBOutlet var H2Label: [UILabel]! {        
        didSet {            
            styleH2Label(H2Label)            
        }        
    }    
    
    @IBOutlet var H3Label: [UILabel]! {        
        didSet {            
            styleH3Label(H3Label)            
        }        
    }    
    
    @IBOutlet var H1Label: [UILabel]! {        
        didSet {            
            styleH1Label(H1Label)            
        }        
    }    
    
    @IBOutlet var H6Label: [UILabel]! {        
        didSet {            
            styleH6Label(H6Label)            
        }        
    }    
    
    @IBOutlet var B1WhiteButtonsButton: [UIButton]! {        
        didSet {            
            styleB1WhiteButtonsButton(B1WhiteButtonsButton)            
        }        
    }    
    
    @IBOutlet var B3TrackerEnumLevelButton: [UIButton]! {        
        didSet {            
            styleB3TrackerEnumLevelButton(B3TrackerEnumLevelButton)            
        }        
    }    
    
    @IBOutlet var B4Button: [UIButton]! {        
        didSet {            
            styleB4Button(B4Button)            
        }        
    }    
    
    @IBOutlet var B1Button: [UIButton]! {        
        didSet {            
            styleB1Button(B1Button)            
        }        
    }    
    
    @IBOutlet var B2Button: [UIButton]! {        
        didSet {            
            styleB2Button(B2Button)            
        }        
    }    
    
    @IBOutlet var B3Button: [UIButton]! {        
        didSet {            
            styleB3Button(B3Button)            
        }        
    }    
    
    @IBOutlet var B1BlackButtonsButton: [UIButton]! {        
        didSet {            
            styleB1BlackButtonsButton(B1BlackButtonsButton)            
        }        
    }    
    
    @IBOutlet var B3TrackerRangeLevelButton: [UIButton]! {        
        didSet {            
            styleB3TrackerRangeLevelButton(B3TrackerRangeLevelButton)            
        }        
    }    
    
    @IBOutlet var T1TextField: [UITextField]! {        
        didSet {            
            styleT1TextField(T1TextField)            
        }        
    }    
    
    func styleP2Label(objects: [UILabel]) {        
        for object in objects {        
            object.font = UIFont (name: primaryFontLight, size: 16)            
            }            
        }    
    
    func styleP1Label(objects: [UILabel]) {        
        for object in objects {        
            object.font = UIFont (name: primaryFontMedium, size: 16)            
            }            
        }    
    
    func styleH2Label(objects: [UILabel]) {        
        for object in objects {        
            object.font = UIFont (name: primaryFontLightItalic, size: 30)            
            }            
        }    
    
    func styleH3Label(objects: [UILabel]) {        
        for object in objects {        
            object.font = UIFont (name: primaryFontBlack, size: 24)            
            }            
        }    
    
    func styleH1Label(objects: [UILabel]) {        
        for object in objects {        
            object.font = UIFont (name: primaryFontMedium, size: 40)            
            }            
        }    
    
    func styleH6Label(objects: [UILabel]) {        
        for object in objects {        
            object.font = UIFont (name: primaryFontLight, size: 23)            
            }            
        }    
    
    func styleB1WhiteButtonsButton(objects: [UIButton]) {        
        for object in objects {        
            object.backgroundColor = baseClearColor            
            object.setTitleColor(baseColorWhite, forState: .Normal)            
            object.titleLabel?.font = UIFont (name: primaryFontBlack, size: 15)            
            object.layer.cornerRadius = 20            
            object.layer.borderColor = baseColorWhite.CGColor            
            object.layer.borderWidth = 1            
            }            
        }    
    
    func styleB3TrackerEnumLevelButton(objects: [UIButton]) {        
        for object in objects {        
            object.setTitleColor(baseColorWhite, forState: .Normal)            
            object.titleLabel?.font = UIFont (name: primaryFontBlack, size: 13)            
            object.layer.cornerRadius = 15            
            }            
        }    
    
    func styleB4Button(objects: [UIButton]) {        
        for object in objects {        
            object.setTitleColor(baseColorWhite, forState: .Normal)            
            object.titleLabel?.font = UIFont (name: primaryFontMedium, size: 16)            
            }            
        }    
    
    func styleB1Button(objects: [UIButton]) {        
        for object in objects {        
            object.titleLabel?.font = UIFont (name: primaryFontBlack, size: 14)            
            }            
        }    
    
    func styleB2Button(objects: [UIButton]) {        
        for object in objects {        
            object.titleLabel?.font = UIFont (name: primaryFontBlack, size: 13)            
            }            
        }    
    
    func styleB3Button(objects: [UIButton]) {        
        for object in objects {        
            object.titleLabel?.font = UIFont (name: primaryFontBlack, size: 13)            
            }            
        }    
    
    func styleB1BlackButtonsButton(objects: [UIButton]) {        
        for object in objects {        
            object.backgroundColor = baseClearColor            
            object.setTitleColor(baseBlackColor, forState: .Normal)            
            object.titleLabel?.font = UIFont (name: primaryFontMedium, size: 13)            
            object.layer.cornerRadius = 20            
            object.layer.borderColor = baseBlackColor.CGColor            
            object.layer.borderWidth = 1            
            }            
        }    
    
    func styleB3TrackerRangeLevelButton(objects: [UIButton]) {        
        for object in objects {        
            object.setTitleColor(baseColorWhite, forState: .Normal)            
            object.titleLabel?.font = UIFont (name: primaryFontBlack, size: 13)            
            object.layer.cornerRadius = 15            
            object.layer.borderColor = baseColorWhite.CGColor            
            object.layer.borderWidth = 1            
            }            
        }    
    
    func attributesForT1TextField() ->  Dictionary<String, AnyObject> {         
        let attributes = [             
            NSFontAttributeName: primaryFontBlack,            
            NSForegroundColorAttributeName: baseBlackColor,            
            NSKernAttributeName: 3            
         ]        
        return attributes        
    }    
    
    func styleT1TextField(objects: [UITextField]) {        
        for object in objects {        
            object.textColor = baseColorWhite            
            object.layer.cornerRadius = 15            
            }            
        }    
    
}