
import Foundation
import UIKit

class SliderStyle : Stylist {
    
    typealias Element = UISlider
    
    var tintColor: UIColor?
    var thumbImage: UIImage?
    var minimumTrackImage: UIImage?
    var maximumTrackImage: UIImage?
    var filledTrackColor: UIColor?
    var emptyTrackColor: UIColor?
    
    enum Properties: String {
        case ThumbImage = "thumbImage"
        case MinimumTrackImage = "minimumTrackImage"
        case MaximumTrackImage = "maximumTrackImage"
        case FilledTrackColor = "filledTrackColor"
        case EmptyTrackColor = "emptyTrackColor"
    }
    
    static let allValues:[Properties] = [.FilledTrackColor,.EmptyTrackColor, .ThumbImage, .MinimumTrackImage, .MaximumTrackImage]
    
    static func serialize(_ spec: [String:AnyObject], resources:CommonResources) throws -> SliderStyle {
        let style = SliderStyle()
        for (key,value) in spec {
            guard let property = SliderStyle.Properties(rawValue: key) else {
                print("StyleKit: Warning: StyleKit does not support \(key) on \(Element.self). Ignored.")
                continue
            }
            switch property {
            case .ThumbImage:
                if let imageKey = value as? String, let imageName = resources.imageNames[imageKey],
                    let image = UIImage(named:imageName){
                    style.thumbImage = image
                }
            case .MinimumTrackImage:
                if let imageKey = value as? String, let imageName = resources.imageNames[imageKey],
                    let image = UIImage(named:imageName){
                    style.minimumTrackImage = image
                }
            case .MaximumTrackImage:
                if let imageKey = value as? String, let imageName = resources.imageNames[imageKey],
                    let image = UIImage(named:imageName){
                    style.maximumTrackImage = image
                }
            case .FilledTrackColor:
                if let colorKey = value as? String, let color = resources.colors[colorKey] {
                    style.filledTrackColor = color
                }
            case .EmptyTrackColor:
                if let colorKey = value as? String, let color = resources.colors[colorKey] {
                    style.emptyTrackColor = color
                }
            }
            
        }
        return style
    }

}

extension UISlider {
    
    func applyStyle(_ style:SliderStyle, resources:CommonResources) {
        for property in SliderStyle.allValues {
            switch property {
            case .ThumbImage:
                if let image = style.thumbImage {
                    self.setThumbImage(image, for: .normal)
                }
            case .MinimumTrackImage:
                if let image = style.minimumTrackImage {
                    self.setMinimumTrackImage(image, for: .normal)
                }
            case .MaximumTrackImage:
                if let image = style.maximumTrackImage {
                    self.setMaximumTrackImage(image, for: .normal)
                }
            case .FilledTrackColor:
                if let color = style.filledTrackColor {
                    self.minimumTrackTintColor = color
                }
            case .EmptyTrackColor:
                if let color = style.emptyTrackColor {
                    self.maximumTrackTintColor = color
                }
            }
        }
    }
    
}

