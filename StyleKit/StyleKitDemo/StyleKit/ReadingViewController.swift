import UIKit


class ReadingViewController: UIViewController {

    @IBOutlet weak var textView: UITextView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Reader"
        self.setDayTimeReading()
    }
    
    
    @IBAction func switchChanged(_ sender: AnyObject) {
        guard let theSwitch = sender as? UISwitch else {
            return
        }

        if theSwitch.isOn {
            UIView.animate(withDuration: 0.25, animations: {
                self.setNightTimeReading()
            }) 
        } else {
            UIView.animate(withDuration: 0.25, animations: {
                self.setDayTimeReading()
            }) 
        }
    }
    
    func setNightTimeReading() {
        self.textView.styleTag = "NightTimeReading"
        self.view.styleTag = "NightTimeReading"
    }

    func setDayTimeReading() {
        self.textView.styleTag = "DayTimeReading"
        self.view.styleTag = "DayTimeReading"
    }

}
