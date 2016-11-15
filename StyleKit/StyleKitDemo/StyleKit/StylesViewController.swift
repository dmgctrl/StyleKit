
import UIKit
import StyleKit

class StylesViewController: UIViewController {

    @IBOutlet weak var tableView: UITableView!
    @IBOutlet weak var button: UIButton!

    var sectionHeaders = Array(Style.sharedInstance.styleMap.keys)
    var styleMap = Style.sharedInstance.styleMap
    var resources:[String:AnyObject] = ["Colors":Array(Style.sharedInstance.resources.colors.keys) as AnyObject,
                                        "Fonts":Array(Style.sharedInstance.resources.fontLabels.keys) as AnyObject,
                                        "Images":Array(Style.sharedInstance.resources.imageNames.keys) as AnyObject]
    
    
    @IBAction func buttonTapped(_ sender: AnyObject) {
        Utils.downloadStyleFile()
    }

    override func viewDidLoad() {
        super.viewDidLoad()

        title = "Styles Preview"
        Style.sharedInstance.addSubscriber(self)
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()

    }
        
    func updateUI() {
        sectionHeaders = Array(Style.sharedInstance.styleMap.keys)
        styleMap = Style.sharedInstance.styleMap
        resources = ["Colors":Array(Style.sharedInstance.resources.colors.keys) as AnyObject,
                                            "Fonts":Array(Style.sharedInstance.resources.fontLabels.keys) as AnyObject,
                                            "Images":Array(Style.sharedInstance.resources.imageNames.keys) as AnyObject]
        tableView.reloadData()
    }
}

extension StylesViewController: StyleKitSubscriber {
    func update() {
        self.updateUI()
    }
}

extension StylesViewController: UITableViewDelegate {

    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        
        switch sectionHeaders[indexPath.section] {
        case .button, .view, .textField:
            return 70.0
        default:
            return 54.0
        }
    }
}

extension StylesViewController: UITableViewDataSource {
    
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        if let styles = styleMap[sectionHeaders[section]] {
            return styles.keys.count
        }
        return 0
    }
    
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let sectionHeader = sectionHeaders[indexPath.section]
        
        let cell = tableView.dequeueReusableCell(withIdentifier: "\(sectionHeader.rawValue)Cell", for: indexPath)

        var styleTag = ""
        if let styles = styleMap[sectionHeader] {
            let allTags = Array(styles.keys)
            styleTag = allTags[indexPath.row]
            
            switch sectionHeader {
            case .button:
                (cell as! ButtonTableViewCell).button.styleTag = styleTag
                (cell as! ButtonTableViewCell).button.setTitle(styleTag, for: .normal)
            case .segmentedControl:
                (cell as! SegmentedControlsTableViewCell).segmentedControl.styleTag = styleTag
                (cell as! SegmentedControlsTableViewCell).label.text = styleTag
            case .textField:
                (cell as! TextFieldsTableViewCell).textField.styleTag = styleTag
                (cell as! TextFieldsTableViewCell).textField.text = styleTag
            case .label:
                (cell as! LabelsTableViewCell).label.styleTag = styleTag
                (cell as! LabelsTableViewCell).label.text = styleTag
            case .slider:
                (cell as! SlidersTableViewCell).slider.styleTag = styleTag
                (cell as! SlidersTableViewCell).label.text = styleTag
            case .stepper:
                (cell as! SteppersTableViewCell).stepper.styleTag = styleTag
                (cell as! SteppersTableViewCell).label.text = styleTag
            case .progressView:
                (cell as! ProgressViewsTableViewCell).progressView.styleTag = styleTag
                (cell as! ProgressViewsTableViewCell).label.text = styleTag
            case .view:
                (cell as! ViewsTableViewCell).view.styleTag = styleTag
                (cell as! ViewsTableViewCell).label.text = styleTag
            case .textView:
                (cell as! TextViewsTableViewCell).textView.styleTag = styleTag
                (cell as! TextViewsTableViewCell).textView.text = styleTag
            }
        }
                
        return cell
    }
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return sectionHeaders.count
    }
    
    func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return sectionHeaders[section].rawValue
    }
}
