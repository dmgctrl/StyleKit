//Theme Generated:2015-10-20 16:22:45

import UIKit

class Theme: NSObject {

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
            object.font = UIFont (name: "BrandonGrotesque-Bold", size: 14)            
            }            
        }    
    
    func styleH7Label(labels: [UILabel]) {        
        for object in H7Label {        
            object.font = UIFont (name: "BrandonGrotesque-Light", size: 20)            
            }            
        }    
    
}