//Theme Generated:2015-10-21 16:16:12

import UIKit

class Theme: NSObject {

    let primaryFontMedium: String = "BrandonGrotesque-Medium"    
    let primaryFontBlack: String = "BrandonGrotesque-Black"    
    let primaryFontLight: String = "BrandonGrotesque-Light"    
    let primaryFontBold: String = "BrandonGrotesque-Bold"    
    
    let secondaryColor = UIColor(red: 255.00, green: 255.00, blue: 255.00, alpha: 1.00)    
    let primaryColor = UIColor(red: 220.00, green: 20.00, blue: 60.00, alpha: 1.00)    
    
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
            }            
        }    
    
}