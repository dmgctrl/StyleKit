//Theme Generated:2015-10-22 10:41:42

import UIKit

class Theme: NSObject {

    let primaryFontMedium: String = "BrandonGrotesque-Medium"    
    let primaryFontBlack: String = "BrandonGrotesque-Black"    
    let primaryFontLight: String = "BrandonGrotesque-Light"    
    let primaryFontBold: String = "BrandonGrotesque-Bold"    
    
    let secondaryColor = UIColor(red: 0.00, green: 0.00, blue: 0.00, alpha: 1.00)    
    let primaryColor = UIColor(red: 1.00, green: 1.00, blue: 1.00, alpha: 1.00)    
    
    @IBOutlet var H1Label: [UILabel]! {        
        didSet {            
            styleH1Label(H1Label)            
        }        
    }    
    
    @IBOutlet var H7Label: [UILabel]! {        
        didSet {            
            styleH7Label(H7Label)            
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
    
    func styleH1Label(labels: [UILabel]) {        
        for object in H1Label {        
            object.font = UIFont (name: primaryFontBold, size: 14)            
            object.textColor = secondaryColor            
            }            
        }    
    
    func styleH7Label(labels: [UILabel]) {        
        for object in H7Label {        
            object.font = UIFont (name: primaryFontLight, size: 34)            
            object.textColor = primaryColor            
            }            
        }    
    
    func styleB1Button(buttons: [UIButton]) {        
        for object in B1Button {            
            object.backgroundColor = secondaryColor            
            object.setTitleColor(primaryColor, forState: .Normal)            
            object.titleLabel?.font = UIFont (name: primaryFontBold, size: 34)            
            object.layer.cornerRadius = 22            
            }            
        }    
    
    func styleB2Button(buttons: [UIButton]) {        
        for object in B2Button {            
            object.backgroundColor = primaryColor            
            object.setTitleColor(secondaryColor, forState: .Normal)            
            object.layer.cornerRadius = 8            
            }            
        }    
    
}