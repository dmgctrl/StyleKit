//Theme Generated:2015-10-21 11:47:43

import UIKit

class Theme: NSObject {

    let primaryFontMedium: String = "BrandonGrotesque-Medium"    
    let primaryFontBlack: String = "BrandonGrotesque-Black"    
    let primaryFontLight: String = "BrandonGrotesque-Light"    
    let primaryFontBold: String = "BrandonGrotesque-Bold"    
    
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
    
    func styleH1Label(labels: [UILabel]) {        
        for object in H1Label {        
            object.font = UIFont (name: primaryFontBold, size: 14)            
            }            
        }    
    
    func styleH7Label(labels: [UILabel]) {        
        for object in H7Label {        
            object.font = UIFont (name: primaryFontLight, size: 20)            
            object.textColor = 220,20,60            
            }            
        }    
    
}