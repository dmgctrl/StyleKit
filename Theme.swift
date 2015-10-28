//Theme Generated:2015-10-28 15:44:58

import UIKit

class Theme: NSObject {

    static let sharedInstance = Theme()    
    
    let primaryFontMedium: String = "BrandonGrotesque-Medium"    
    let primaryFontBlack: String = "BrandonGrotesque-Black"    
    let primaryFontLight: String = "BrandonGrotesque-Light"    
    let primaryFontLightItalic: String = "BrandonGrotesque-LightItalic"    
    let primaryFontBold: String = "BrandonGrotesque-Bold"    
    
    let baseColorRedLight = UIColor(red: 250.00, green: 110.00, blue: 92.00, alpha: 1.00)    
    let baseColorGreyLight = UIColor(red: 194.00, green: 194.00, blue: 194.00, alpha: 1.00)    
    let activityTertiary = UIColor(red: 185.00, green: 80.00, blue: 71.00, alpha: 1.00)    
    let baseColorBlueMedium = UIColor(red: 77.00, green: 191.00, blue: 213.00, alpha: 1.00)    
    let baseColorWhite = UIColor(red: 255.00, green: 255.00, blue: 255.00, alpha: 1.00)    
    let activitySecondary = UIColor(red: 219.00, green: 96.00, blue: 85.00, alpha: 1.00)    
    let baseColorRedDark = UIColor(red: 197.00, green: 35.00, blue: 38.00, alpha: 1.00)    
    let baseColorGreyDark = UIColor(red: 102.00, green: 102.00, blue: 102.00, alpha: 1.00)    
    let baseColorRedMedium = UIColor(red: 234.00, green: 75.00, blue: 44.00, alpha: 1.00)    
    let activityPrimary = UIColor(red: 242.00, green: 114.00, blue: 101.00, alpha: 1.00)    
    let baseColorGreyMedium = UIColor(red: 135.00, green: 135.00, blue: 135.00, alpha: 1.00)    
    let baseColorBlueDark = UIColor(red: 65.00, green: 162.00, blue: 182.00, alpha: 1.00)    
    let baseColorBlueLight = UIColor(red: 73.00, green: 208.00, blue: 223.00, alpha: 1.00)    
    let baseColorGreyVeryLight = UIColor(red: 62.00, green: 62.00, blue: 62.00, alpha: 1.00)    
    
    let buttonImage1 = UIImage(named: "black_button_image")    
    
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
    
    @IBOutlet var T1TextField: [UITextField]! {        
        didSet {            
            styleT1TextField(T1TextField)            
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
    
    func styleB1Button(objects: [UIButton]) {        
        for object in objects {        
            object.titleLabel?.font = UIFont (name: primaryFontBlack, size: 19)            
            }            
        }    
    
    func styleB2Button(objects: [UIButton]) {        
        for object in objects {        
            object.titleLabel?.font = UIFont (name: primaryFontBlack, size: 17)            
            }            
        }    
    
    func styleB3Button(objects: [UIButton]) {        
        for object in objects {        
            object.titleLabel?.font = UIFont (name: primaryFontBlack, size: 17)            
            }            
        }    
    
    func styleT1TextField(objects: [UITextField]) {        
        for object in objects {        
            object.layer.borderWidth = 1            
            }            
        }    
    
}