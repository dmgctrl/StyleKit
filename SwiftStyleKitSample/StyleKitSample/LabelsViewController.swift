import UIKit

class LabelsViewController: UIViewController {
    
    @IBOutlet var labels: [UILabel]! {
        didSet {
            var info = [String: UILabel]()
            for label in labels {
                if let styleTag = label.styleTag {
                    info[styleTag] = label
                }
            }
            Style.sharedInstance.style(withLabelsAndStyles: info)
        }
    }

}
