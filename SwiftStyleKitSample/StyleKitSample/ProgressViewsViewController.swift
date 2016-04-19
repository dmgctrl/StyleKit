import UIKit

class ProgressViewsViewController: UIViewController {

    @IBOutlet var progressViews: [UIProgressView]! {
        didSet {
            var info = [String: UIProgressView]()
            for progressView in progressViews {
                if let styleTag = progressView.styleTag {
                    info[styleTag] = progressView
                }
            }
            Style.sharedInstance.style(withProgressViewsAndStyles: info)
        }
    }
    
    @IBOutlet weak var slider: UISlider!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func sliderValueChanged(sender: UISlider) {
        for progressView in progressViews {
            progressView.setProgress(slider.value, animated: true)
        }
    }

}
