//
//  ButtonsViewController.swift
//  StyleKitSample
//
//  Created by Van Nguyen on 4/12/16.
//  Copyright © 2016 Tonic Design. All rights reserved.
//

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
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
