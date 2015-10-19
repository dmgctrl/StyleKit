//Theme Generated:2015-10-19 12:05:40

import UIKit

class Theme: NSObject {

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
    
    @IBOutlet var B3Button: [UIButton]! {        
        didSet {            
            styleB3Button(B3Button)            
        }        
    }    
    
    func styleH7Label(labels: [UILabel]) {        
        for object in H7Label {        
            object.font = UIFont (name: "BrandonGrotesque-Light", size: 20)            
            object.textColor = UIColor(red: 1.00, green: 1.00, blue: 1.00, alpha: 1.00)            
            }            
        }    
    
    func styleB1Button(buttons: [UIButton]) {        
        for object in B1Button {            
            object.backgroundColor = UIColor(red: 0.00, green: 0.00, blue: 1.00, alpha: 1.00)            
            object.setTitleColor(UIColor(red: 1.00, green: 1.00, blue: 1.00, alpha: 1.00), forState: .Normal)            
            }            
        }    
    
    func styleB2Button(buttons: [UIButton]) {        
        for object in B2Button {            
            object.backgroundColor = UIColor(red: 1.00, green: 1.00, blue: 1.00, alpha: 1.00)            
            object.layer.cornerRadius = 5            
            object.layer.borderColor = UIColor(red: 0.00, green: 0.00, blue: 0.00, alpha: 1.00).CGColor            
            object.layer.borderWidth = 2            
            }            
        }    
    
    func styleB3Button(buttons: [UIButton]) {        
        for object in B3Button {            
            object.backgroundColor = UIColor(red: 224.00, green: 224.00, blue: 224.00, alpha: 1.00)            
            object.setTitleColor(UIColor(red: 0.00, green: 0.00, blue: 0.00, alpha: 1.00), forState: .Normal)            
            object.layer.cornerRadius = 10            
            object.layer.borderColor = UIColor(red: 0.00, green: 0.00, blue: 0.00, alpha: 1.00).CGColor            
            object.layer.borderWidth = 2            
            }            
        }    
    
}