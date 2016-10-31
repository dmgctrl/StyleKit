# StyleKit

StyleKit is a iOS library that styles native controls with a CSS like JSON format.  This simplifies and centralizes your styling code.  With StyleKit, you can replace many complicated lines of Swift with a few lines of StyleKit JSON.

The StyleKit API additionally supports the ability to dynamically update styles in your app by changing your StyleKit JSON. Controllers can subscribe to style changes and update their UI elements.

## Install StyleKit using Carthage

`github "dmgctrl/StyleKit"`

## Style Elements

To style a UI element using StyleKit, you set its 'styleTag' property, to a tag defined in the stylesheet. The example below sets a UIButton's style in the `viewDidLoad` of view controller.

```swift
@IBOutlet weak var button: UIButton!

override func viewDidLoad() {
    super.viewDidLoad()
    button.styleTag = "B3"
}
```

## Usage

StyleKit by default looks for a stylesheet named `Style.json` in the bundle. The location and name of the stylesheet can be customized by setting an alternate location in your apps Info.plist. The location may be specified as a directory (implied file name of Style.json) or as directory/filename.

	<key>StyleKit-StylesheetLocation</key>
	<string>SpecialStyle.json</string>

In the example above, StyleKit will will attempt to load styles from the file `SpecialStyle.json` in the apps Documents directory.

Below are examples for the currently supported features of the StyleKit JSON.

#### Fonts

```JSON

"Fonts": {
    "fontKey": "font-bundle-identifier"
}

```

#### Font Styles

```JSON

"fontStyle": {
    "font": "primaryFontLightItalic",
    "size": 20
}

```

#### Colors

You can specify a color with either a Hex value or an RGB value. Alpha is optional in both (default is 1.0). See examples below:

```JSON

"Colors": {
    "colorKey": {
        "red": 250,   // RGB Value between 1-255
        "green": 110, // RGB Value between 1-255
        "blue": 92,   // RGB Value between 1-255
        "alpha": 1    // Alpha Value between 0.0-1.0
    },
    "colorKey2": {
        "hex": "#000000", // Hex value
        "alpha": 1        // Alpha Value between 0.0-1.0
    }
}

```

#### Images

```JSON

"Images": {
    "imageKey": "image-bundle-identifier"
}

```

#### Views

```JSON

"Views": {
    "viewName": {
        "backgroundColor": "blueColor",
        "borderColor": "blackColor",
        "borderWidth": 5,
        "cornerRadius": 5
    }
}

```

#### Labels

To use attributes the label must be set to attributed text in Interface Builder.

```JSON

"Labels": {
    "H1": {
        "textColor": "whiteColor",
        "textAlignment": "Center",
        "attributes": {
            "fontStyle": {
                "font": "primaryFontLight",
                "size": 34
            },
            "tracking": 100,
            "lineSpacing": 25,
            "ligature": 1
        }
    }
}

```

#### Buttons

To use titleColor for button state you must set the button as "Custom" type in Interface Builder. Currently supports button states ` normal `, ` selected `, `  highlighted `

```JSON

"Buttons": {
    "primaryButton": {
        "borderColor": "whiteColor",
        "borderWidth": 3,
        "cornerRadius": 10,
        "fontStyle": {
            "font": "primaryFontMedium",
            "size": 16
        },
        "normalState": {
            "backgroundColor": "blackColor",
            "textColor": "whiteColor"
        },
        "selectedState": {
            "backgroundColor": "blackColor",
            "textColor": "purpleColor"
        },
        "highlightedState": {
            "backgroundColor": "blackColor",
            "textColor": "whiteColor"
        }
    }
}

```

#### TextFields

* textAlignment values : ` "Left", "Right", "Center", "Justified", "Natural" `
* borderStyle values : ` "None", "Line", "Bezel", "RoundedRect" `

```JSON
"TextFields": {
    "T1": {
        "fontStyle": {
            "font": "primaryFontMedium",
            "size": 15
        },
        "textColor": "whiteColor",
        "backgroundColor": "purpleColor",
        "borderColor": "blackColor",
        "textAlignment": "Center",
        "borderWidth": 2,
        "cornerRadius": 5,
        "borderStyle": "RoundedRect"
    }
}

```
#### TextViews

* textAlignment values : ` "Left", "Right", "Center", "Justified", "Natural" `

```JSON
"TextViews": {
       "TV1": {
           "textColor": "blueColor",
           "textAlignment": "Center",
           "attributes": {
               "fontStyle": {
                   "font": "primaryFontMedium",
                   "size": 22
               },
               "tracking": 100,
               "lineSpacing": 5,
               "ligature": 0
           }
       }
   },

```

#### SegmentedControls

```JSON
"SegmentedControls": {
    "default": {
          "fontStyle": {
              "font": "primaryFontLight",
              "size": 13
          },
          "tintColor": "baseColorBlack",
          "normalState": {
              "textColor": "whiteColor"
          },
          "selectedState": {
              "textColor": "purpleColor"
          }
    }
}

```

#### Sliders

* Note: if both the track tint colors and the track images are specified, the tint colors will override the images.

```JSON
    "Sliders": {
        "S1": {
            "minimumTrackTintColor": "purpleColor",
            "maximumTrackTintColor": "whiteColor",
            "thumbImage": "thumbImageDefault"
        },
        "S2": {
          "minimumTrackImage": "defaultFilledTrackImage",
          "maximumTrackImage": "defaultEmptyTrackImage"
        }
    }

```

## Dynamic Updates

Dynamic updates to tagged ui elements are possible by updating the style JSON and communicating the change. Since the bundle is readonly, you must first place your style.json in the app's documents directory (or other writable location) and tell StyleKit where you placed it by adding a key/value entry in the apps info.plist.

Now when you make changes to style json, you need to tell StyleKit that the stylesheet has changed.

  ```
  StyleKit.sharedInstance.refresh()
  ```

The new stylesheet will **not** automatically get applied to views which have already been tagged/styled. View controllers or objects may register to receive notification of stylesheet changes by registering as a subscriber.

  ```
  StyleKit.sharedInstance.addSubscriber(self)
   ```

  To restyle a view which has already been tagged/styled, set a different tag or just call `style()` for a view which already has a tag.

  ```swift
      button.styleTag = "B3"
      // or
      button.style()
  }
  ```
