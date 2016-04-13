import UIKit

class TextFieldsViewController: UIViewController {
    
    @IBOutlet var textFields: [UITextField]! {
        didSet {
            var info = [String: UITextField]()
            for textField in textFields {
                if let styleTag = textField.styleTag {
                    info[styleTag] = textField
                }
            }
            Style.sharedInstance.style(withTextFieldsAndStyles: info)
        }
    }

}
