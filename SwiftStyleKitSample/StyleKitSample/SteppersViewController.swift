import UIKit

class SteppersViewController: UIViewController {
    
    @IBOutlet var steppers: [UIStepper]! {
        didSet {
            var info = [String: UIStepper]()
            for stepper in steppers {
                if let styleTag = stepper.styleTag {
                    info[styleTag] = stepper
                }
            }
            Style.sharedInstance.style(withSteppersAndStyles: info)
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

}
