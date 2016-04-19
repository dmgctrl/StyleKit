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
    
    @IBOutlet weak var slider1: UISlider!
    @IBOutlet weak var slider2: UISlider!
    @IBOutlet weak var label1: UILabel!
    @IBOutlet weak var label2: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        self.slider1.maximumValue = 100
        self.slider1.minimumValue = 0
        self.slider1.value = 0
        
        self.slider2.maximumValue = 50
        self.slider2.minimumValue = 0
        self.slider2.value = 0
        
        self.label1.text = "\(self.slider1.value) / \(self.slider1.maximumValue)"
        self.label2.text = "\(self.slider2.value) / \(self.slider2.maximumValue)"
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func sliderOneValueChanged(sender: UISlider) {
        self.label1.text = "\(self.slider1.value) / \(self.slider1.maximumValue)"
    }

    @IBAction func sliderTwoValueChanged(sender: UISlider) {
        self.label2.text = "\(self.slider2.value) / \(self.slider2.maximumValue)"
    }
}
