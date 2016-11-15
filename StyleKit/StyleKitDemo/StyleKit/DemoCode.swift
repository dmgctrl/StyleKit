
import Foundation
import StyleKit

extension Utils {
    
    // WARNING: Replace with an URL to your remote stylesheet
    static let styleKitLink = "https://www.mystylesheetserver.com/location/Style.json"
    
    static func copyStyleFileFromBundle() {
        
        if let relativePath = Bundle.main.infoDictionary?[Style.styleSheetLocationKey] as? String,
        let srcDir = Bundle.main.url(forResource: "Style", withExtension: "json"),
            let destDir = Utils.documentDirectory?.appendingPathComponent(relativePath) {
            Utils.copyStyleFile(from: srcDir, to: destDir)
        }
    }
    
    static func copyStyleFile(from srcURL: URL, to destURL: URL) {
        let fileManager = FileManager.default
        
        if fileManager.fileExists(atPath: destURL.path) {
            do {
                try fileManager.removeItem(at: destURL)
            } catch let error {
                print(error)
            }
        }
        
        do {
            if !destURL.path.hasSuffix(".json") {
                try fileManager.createDirectory(at: destURL, withIntermediateDirectories: false, attributes: nil)
                try fileManager.copyItem(at: srcURL, to: destURL.appendingPathComponent("Style.json"))
            } else {
                try fileManager.copyItem(at: srcURL, to: destURL)
            }
        } catch let error {
            print(error)
        }
    }
    
    static func downloadStyleFile() {
        if let string = Bundle.main.infoDictionary?[Style.styleSheetLocationKey] as? String {
            if let url = URL(string:Utils.styleKitLink) {
                URLSession.shared.downloadTask(with: url, completionHandler: { tempFileDirectory, response, error in
                    if error == nil {
                        if let srcDirectory = tempFileDirectory, let destDirectory = Utils.documentDirectory?.appendingPathComponent(string) {
                            Utils.copyStyleFile(from: srcDirectory, to: destDirectory)
                            DispatchQueue.main.async(execute: {
                                Style.sharedInstance.refresh()
                            })
                        }
                    } else {
                        print("\(error)")
                    }
                }).resume()
            }
        }
    }
    
}
