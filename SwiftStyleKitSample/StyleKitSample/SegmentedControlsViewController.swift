//
//  SegmentedControlsViewController.swift
//  StyleKitSample
//
//  Created by Van Nguyen on 4/12/16.
//  Copyright © 2016 Tonic Design. All rights reserved.
//

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
