//
//  UIView+StyleKit.swift
//  StyleKitSample
//
//  Created by Van Nguyen on 4/5/16.
//  Copyright © 2016 Tonic Design. All rights reserved.
//

import UIKit

extension UIView {
    private struct AssociatedKeys {
        static var styleTag = ""
    }
    
    var styleTag: String? {
        get {
            return objc_getAssociatedObject(self, &AssociatedKeys.styleTag) as? String
        }
        
        set {
            if let newValue = newValue {
                objc_setAssociatedObject(
                    self,
                    &AssociatedKeys.styleTag,
                    newValue as NSString?,
                    .OBJC_ASSOCIATION_RETAIN_NONATOMIC
                )
            }
        }
    }
}
