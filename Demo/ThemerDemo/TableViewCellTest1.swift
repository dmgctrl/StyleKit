import Foundation
import UIKit

class TableViewCell1: UITableViewCell {
    
    let theme = Theme.sharedInstance
    
    @IBOutlet var titleLabel: UILabel!
    @IBOutlet weak var buttonView: UIImageView!
    
    override func awakeFromNib() {
        theme.styleH2Label([self.titleLabel])
        buttonView.image = theme.buttonImage1
    }
    
}