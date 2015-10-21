//Theme Generated:2015-10-21 15:38:37

import UIKit

class Theme: NSObject {

    let primaryFontMedium: String = "BrandonGrotesque-Medium"    
    let primaryFontBlack: String = "BrandonGrotesque-Black"    
    let primaryFontLight: String = "BrandonGrotesque-Light"    
    let primaryFontBold: String = "BrandonGrotesque-Bold"    
    
    let primaryColor: = UIColor(red: 220.00, green: 20.00, blue: 60.00, alpha: 1.00)    
    
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
            object.font = UIFont (name: BrandonGrotesque-Bold, size: 14)            
            object.textColor = 220,20,60,1            
            }            
        }    
    
    func styleH7Label(labels: [UILabel]) {        
        for object in H7Label {        
            object.font = UIFont (name: BrandonGrotesque-Light, size: 20)            
            object.textColor = 220,20,60            
            }            
        }    
    
    func styleB1Button(buttons: [UIButton]) {        
        for object in B1Button {            
            }            
        }    
    
}