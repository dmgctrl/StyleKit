import UIKit

class SlidersViewController: UIViewController {

    @IBOutlet var sliders: [UISlider]! {
        didSet {
            var info = [String: UISlider]()
            for slider in sliders {
                if let styleTag = slider.styleTag {
                    info[styleTag] = slider
                }
            }
            Style.sharedInstance.style(withSlidersAndStyles: info)
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
