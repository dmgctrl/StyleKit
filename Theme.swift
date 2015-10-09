import UIKit

class Theme: NSObject {

    @IBOutlet var h1Label: [UILabel]! {        
        didSet {            
            h1LabelStyle()            
        }        
    }    
    
    func h1LabelStyle() {    
        for object in h1Label {        
            object.font = UIFont (name: "Asul", size: 34)            
            object.textColor = UIColor(red: 1.00, green: 0.000000, blue: 0.00, alpha: 1.00)            
        }
    }    
}