//Theme Generated:2015-10-13 16:38:42

import UIKit

class Theme: NSObject {

    @IBOutlet var H1Label: [UILabel]! {        
        didSet {            
            styleH1Label(H1Label)            
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
    
    @IBOutlet var Button1: [UIButton]! {        
        didSet {            
            styleButton1(Button1)            
        }        
    }    
    
    @IBOutlet var Button2: [UIButton]! {        
        didSet {            
            styleButton2(Button2)            
        }        
    }    
    
    @IBOutlet var Button3: [UIButton]! {        
        didSet {            
            styleButton3(Button3)            
        }        
    }    
    
    func styleH1Label(labels: [UILabel]) {        
        for object in H1Label {        
            object.font = UIFont (name: "Asul", size: 34)            
            object.textColor = UIColor(red: 1.00, green: 0.00, blue: 0.00, alpha: 1.00)            
            }            
        }    
    
    func styleH2Label(labels: [UILabel]) {        
        for object in H2Label {        
            object.font = UIFont (name: "Asul", size: 24)            
            object.textColor = UIColor(red: 0.00, green: 1.00, blue: 0.00, alpha: 1.00)            
            }            
        }    
    
    func styleH3Label(labels: [UILabel]) {        
        for object in H3Label {        
            object.font = UIFont (name: "Asul", size: 14)            
            object.textColor = UIColor(red: 1.00, green: 1.00, blue: 0.00, alpha: 1.00)            
            }            
        }    
    
    func styleButton1(buttons: [UIButton]) {        
        for object in Button1 {            
            object.backgroundColor = UIColor(red: 0.00, green: 0.00, blue: 1.00, alpha: 1.00)            
            object.setTitleColor(UIColor(red: 1.00, green: 0.00, blue: 0.00, alpha: 1.00), forState: .Normal)            
            }            
        }    
    
    func styleButton2(buttons: [UIButton]) {        
        for object in Button2 {            
            object.backgroundColor = UIColor(red: 0.00, green: 1.00, blue: 0.00, alpha: 1.00)            
            object.layer.cornerRadius = 5            
            object.layer.borderColor = UIColor(red: 1.00, green: 0.00, blue: 0.00, alpha: 1.00).CGColor            
            object.layer.borderWidth = 2            
            }            
        }    
    
    func styleButton3(buttons: [UIButton]) {        
        for object in Button3 {            
            object.backgroundColor = UIColor(red: 224.00, green: 224.00, blue: 224.00, alpha: 1.00)            
            object.setTitleColor(UIColor(red: 0.00, green: 0.00, blue: 0.00, alpha: 1.00), forState: .Normal)            
            object.layer.cornerRadius = 10            
            object.layer.borderColor = UIColor(red: 0.00, green: 0.00, blue: 0.00, alpha: 1.00).CGColor            
            object.layer.borderWidth = 2            
            }            
        }    
    
}