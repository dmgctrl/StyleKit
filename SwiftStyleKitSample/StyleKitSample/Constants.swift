import Foundation

enum FontProperties: String {
    case Name = "font"
    case Size = "size"
}

enum LabelProperties: String {
    case FontStyle = "fontStyle"
}

enum ButtonProperties: String {
    case FontStyle = "fontStyle"
    case BorderWidth = "borderWidth"
    case BorderColor = "borderColor"
    case CornerRadius = "cornerRadius"
    case Normal = "normal"
}

enum TextFieldProperties: String {
    case FontStyle = "fontStyle"
    case BorderWidth = "borderWidth"
    case BorderColor = "borderColor"
    case CornerRadius = "cornerRadius"
    case TextAlignment = "textAlignment"
    case BorderStyle = "borderStyle"
    case TextColor = "textColor"
}

enum SegmentedControlProperties: String {
    case FontStyle = "fontStyle"
    case NormalState = "normalState"
    case SelectedState = "selectedState"
    case TintColor = "tintColor"
}

enum SliderProperties: String {
    case MinimumTrackTintColor = "minimumTrackTintColor"
    case MaximumTrackTintColor = "maximumTrackTintColor"
    case ThumbImage = "thumbImage"
    case MinimumTrackImage = "minimumTrackImage"
    case MaximumTrackImage = "maximumTrackImage"
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