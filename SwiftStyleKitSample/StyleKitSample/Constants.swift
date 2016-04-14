import Foundation

enum FontProperties: String {
    case Name = "font"
    case Size = "size"
}

enum LabelProperties: String {
    case FontStyle = "fontStyle"
    
    init?(rawValue: String) {
        switch rawValue {
            case "fontStyle":
                self = .FontStyle
            default:
                return nil
        }
    }
}

enum ButtonProperties: String {
    case FontStyle = "fontStyle"
    case BorderWidth = "borderWidth"
    case BorderColor = "borderColor"
    case CornerRadius = "cornerRadius"
    case Normal = "normal"
    
    init?(rawValue: String) {
        switch rawValue {
            case "fontStyle":
                self = .FontStyle
            case "borderWidth":
                self = .BorderWidth
            case "borderColor":
                self = .BorderColor
            case "cornerRadius":
                self = .CornerRadius
            case "normal":
                self = .Normal
            default:
                return nil
        }
    }
}

enum TextFieldProperties: String {
    case FontStyle = "fontStyle"
    case BorderWidth = "borderWidth"
    case BorderColor = "borderColor"
    case CornerRadius = "cornerRadius"
    case TextAlignment = "textAlignment"
    case BorderStyle = "borderStyle"
    case TextColor = "textColor"
    
    init?(rawValue: String) {
        switch rawValue {
            case "fontStyle":
                self = .FontStyle
            case "borderWidth":
                self = .BorderWidth
            case "borderColor":
                self = .BorderColor
            case "cornerRadius":
                self = .CornerRadius
            case "borderStyle":
                self = .BorderStyle
            case "textColor":
                self = .TextColor
            case "textAlignment":
                self = .TextAlignment
            default:
                return nil
        }
    }
}

enum SegmentedControlProperties: String {
    case FontStyle = "fontStyle"
    case NormalState = "normalState"
    case SelectedState = "selectedState"
    case TintColor = "tintColor"
    
    init?(rawValue: String) {
        switch rawValue {
            case "fontStyle":
                self = .FontStyle
            case "normalState":
                self = .NormalState
            case "selectedState":
                self = .SelectedState
            case "tintColor":
                self = .TintColor
            default:
                return nil
        }
    }
}

enum SliderProperties: String {
    case FilledTrackColor = "filledTrackColor"
    case EmptyTrackColor = "emptyTrackColor"
    case ThumbImage = "thumbImage"
    case FilledTrackImage = "filledTrackImage"
    case EmptyTrackImage = "emptyTrackImage"
    
    init?(rawValue: String) {
        switch rawValue {
            case "filledTrackColor":
                self = .FilledTrackColor
            case "emptyTrackColor":
                self = .EmptyTrackColor
            case "thumbImage":
                self = .ThumbImage
            case "filledTrackImage":
                self = .FilledTrackImage
            case "emptyTrackImage":
                self = .EmptyTrackImage
            default:
                return nil
        }
    }
}

enum ColorProperties: String {
    case Red = "red"
    case Green = "green"
    case Blue = "blue"
    case Alpha = "alpha"
}

enum UIElements: String {
    case SegmentedControls = "SegmentedControls"
    case TextFields = "TextFields"
    case Buttons = "Buttons"
    case Labels = "Labels"
    case Sliders = "Sliders"
}

enum CommonObjects: String {
    case Fonts = "Fonts"
    case Colors = "Colors"
    case Images = "Images"
}

enum CommonProperties: String {
    case TitleColor = "titleColor"
    case TextColor = "textColor"
}