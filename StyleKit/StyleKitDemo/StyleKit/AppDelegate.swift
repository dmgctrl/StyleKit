//
//  AppDelegate.swift
//  StyleKitSample
//
//  Created by Eric Kille on 3/10/16.
//  Copyright © 2016 Tonic Design. All rights reserved.
//

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {        
        
        Utils.copyStyleFileFromBundle()
        return true
    }

}


struct Utils {
    static let documentDirectory = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).last
}
