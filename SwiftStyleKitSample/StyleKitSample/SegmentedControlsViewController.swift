import UIKit

class SegmentedControlsViewController: UIViewController {

    @IBOutlet var segmentedControls: [UISegmentedControl]! {
        didSet {
            var info = [String: UISegmentedControl]()
            for segmentedControl in segmentedControls {
                if let styleTag = segmentedControl.styleTag {
                    info[styleTag] = segmentedControl
                }
            }
            Style.sharedInstance.style(withSegmentedControlsAndStyles: info)
        }
    }

}
