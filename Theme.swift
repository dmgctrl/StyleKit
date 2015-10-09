import UIKit

class Theme: NSObject {

    @IBOutlet var h1Label: [UILabel]! {        
        didSet {            
            h1LabelStyle()            
        }        
    }    
    
    @IBOutlet var h2Label: [UILabel]! {        
        didSet {            
            h2LabelStyle()            
        }        
    }    
    
    func h1LabelStyle() {    
        for object in h1Label {        
            object.font = UIFont (name: "Asul", size: 34)            
            object.textColor = UIColor(red: 1.00, green: 0.000000, blue: 0.00, alpha: 1.00)            
                }                
            }        
        
        func h2LabelStyle() {        
            for object in h2Label {            
                object.font = UIFont (name: "Asul", size: 24)                
                object.textColor = UIColor(red: 0.00, green: 1.000000, blue: 0.00, alpha: 1.00)                
                    }                    
                }            
        }