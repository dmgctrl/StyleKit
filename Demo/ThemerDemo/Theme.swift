//Theme Generated:2015-10-26 08:57:00

import UIKit

class Theme: NSObject {
    
    static let sharedInstance = Theme()
    
    let primaryFontMedium: String = "BrandonGrotesque-Medium"
    let primaryFontBlack: String = "BrandonGrotesque-Black"
    let primaryFontLight: String = "BrandonGrotesque-Light"
    let primaryFontLightItalic: String = "BrandonGrotesque-LightItalic"
    let primaryFontBold: String = "BrandonGrotesque-Bold"
    
    let secondaryColor = UIColor(red: 0.00, green: 0.00, blue: 0.00, alpha: 1.00)
    let primaryColor = UIColor(red: 1.00, green: 1.00, blue: 1.00, alpha: 1.00)
    
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
    
    @IBOutlet var T1TextField: [UITextField]! {
        didSet {
            styleT1TextField(T1TextField)
        }
    }
    
    func styleH2Label(objects: [UILabel]) {
        for object in objects {
            object.font = UIFont (name: primaryFontLightItalic, size: 20)
            object.textColor = secondaryColor
        }
    }
    
    func styleH3Label(objects: [UILabel]) {
        for object in objects {
            object.font = UIFont (name: primaryFontBlack, size: 24)
        }
    }
    
    func styleH1Label(objects: [UILabel]) {
        for object in objects {
            object.font = UIFont (name: primaryFontLight, size: 34)
            object.textColor = primaryColor
        }
    }
    
    func styleB4Button(objects: [UIButton]) {
        for object in objects {
            object.setBackgroundImage(buttonImage1, forState: .Normal)
            object.backgroundColor = UIColor.clearColor()
        }
    }
    
    func styleB1Button(objects: [UIButton]) {
        for object in objects {
            object.backgroundColor = secondaryColor
            object.setTitleColor(primaryColor, forState: .Normal)
            object.titleLabel?.font = UIFont (name: primaryFontBold, size: 34)
            object.layer.cornerRadius = 22
        }
    }
    
    func styleB2Button(objects: [UIButton]) {
        for object in objects {
            object.backgroundColor = primaryColor
            object.setTitleColor(secondaryColor, forState: .Normal)
            object.titleLabel?.font = UIFont (name: primaryFontBold, size: 24)
            object.layer.cornerRadius = 8
        }
    }
    
    func styleB3Button(objects: [UIButton]) {
        for object in objects {
            object.setTitleColor(primaryColor, forState: .Normal)
            object.titleLabel?.font = UIFont (name: primaryFontMedium, size: 22)
            object.layer.borderColor = primaryColor.CGColor
            object.layer.borderWidth = 2
        }
    }
    
    func styleT1TextField(objects: [UITextField]) {
        for object in objects {
            object.textColor = primaryColor
            object.backgroundColor = secondaryColor
            object.layer.borderColor = primaryColor.CGColor
            object.layer.borderWidth = 1
        }
    }
    
}