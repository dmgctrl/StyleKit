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

	<key>SKStylesheetLocation</key>
	<string>SpecialStyle.json</string>

In the example above, StyleKit will will attempt to load styles from the file `SpecialStyle.json` in the apps Documents directory.

Below are examples for the currently supported features of the StyleKit JSON.

Fonts, Colors, and Images, are common elements defined to be used elsewhere in the stylesheet.

#### Fonts

```JSON
"Fonts": {
    "primaryFontLight":"BrandonGrotesque-Light",
	"primaryFontMedium":"BrandonGrotesque-Medium",
	"primaryFontBold":"BrandonGrotesque-Bold"	
}
```

The font style keys defined here can be used to style other elements. 
StyleKit will generate a warning if the font cannot be loaded. Make sure to properly configure any custom fonts in your project.

#### Colors

You can specify a color with either a Hex value or an RGB value. Alpha is optional in both (default is 1.0). See examples below:

```JSON

"Colors": {
    "salmonColor": {
        "red": 250,   // RGB Value between 1-255
        "green": 110, // RGB Value between 1-255
        "blue": 92,   // RGB Value between 1-255
        "alpha": 1    // Alpha Value between 0.0-1.0
    },
    "mostlyClearColor": {
        "hex": "#000000", // Hex value
        "alpha": 0.1        // Alpha Value between 0.0-1.0
    }
}

```

The color style keys defined here can be used to style other elements. 

#### Images

```JSON

"Images": {
    "buttonImage1": "image-bundle-identifier"
}

```
The image style keys defined here can be used to style other elements. 
StyleKit will generate a warning if the referenced image cannot be found in the main bundle image assets.

#### Views

```JSON

"Views": {
    "special": {
        "backgroundColor": "lightGrayColor",
        "borderColor": "blueColor",
        "borderWidth": 2,
        "cornerRadius": 10
    },
    "DayTimeReading": {
        "backgroundColor": "whiteColor"
    },
    "NightTimeReading": {
        "backgroundColor": "blackColor"
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
Note the values for "textColor" and "font" refer to keys defined in the Colors and Fonts style elements respectively.

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
Note the values for "borderColor" and "font" refer to keys defined in the Colors and Fonts style elements respectively.


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
```
  <key>SKStylesheetLocation</key>
  <string>NewFolder</string>
```
Now when you make changes to style json, you need to tell StyleKit that the stylesheet has changed by calling `refresh`.

  ```
  StyleKit.sharedInstance.refresh()
  ```

The new stylesheet will **not** automatically get applied to views which have already been tagged/styled. View controllers or objects may be notified of stylesheet changes by registering as a subscriber and implementing the `StyleKitSubscriber` protocol.

  ```
  StyleKit.sharedInstance.addSubscriber(self)
   ```

  Upon notification of an update, view controllers can restyle a view which has already been tagged/styled by resetting the views styleTag property or just call `style()`.

  ```swift
      button.styleTag = "B3"
      // or call style if styleTag has already been set
      button.style()
  }
  ```
