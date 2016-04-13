import UIKit

class ButtonsViewController: UIViewController {
    
    @IBOutlet var buttons: [UIButton]! {
        didSet {
            var info = [String: UIButton]()
            for button in buttons {
                if let styleTag = button.styleTag {
                    info[styleTag] = button
                }
            }
            Style.sharedInstance.style(withButtonsAndStyles: info)
        }
    }

}
