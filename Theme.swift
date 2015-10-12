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
}