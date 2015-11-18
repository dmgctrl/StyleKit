# StyleKit

StyleKit is a native iOS library that styles native controls with a CSS like JSON format. With StyleKit, you can replace many complicated lines of Swift with a few lines of StyleKit JSON. This simplifies and centralizes your styling code, and offers other benefits as well. Styles are wired up to their objects via IBOutlet collections and generates methods per style that can be applied in code if necessary.

## Requirements

1. ` Python ` version 2.7 or newer
2. ` pip ` -  to install ` brew install python ` this will install all of pythons developer tools along with it

## Install StyleKit in New Project

1. ` cd ` Into the root of the project you'd like to install StyleKit
2. add styleKit submodule in ` Libraries/ ` directory ` git submodule add https://github.com/dmgctrl/StyleKit.git Libraries/StyleKit `
3. create ` Styles/ ` in the ` ${TARGET_NAME}/ ` directory of your project
4. add your ` Style.json ` file to the ` Styles/ ` directory
5. Open Xcode project and navigate to your targets ` Build Phases `
6. Add a new ` Run Script ` under the ` Target Dependencies ` build phase
7. Add the following BASH Script :
  * *please note* : this assumes the location of ` Libraries/StyleKit/ ` & ` ${TARGET_NAME}/Style/Style.json ` those requirements must be added as described by the previous instructions or this BASH script must altered to reflect there location.

```

export PATH="$PATH:/usr/local/bin/"

if [ ! -d Libraries/StyleKit/ ]; then
    echo "error: Missing submodules run : $ git submodule update --init"
    exit 1
fi

pip list | grep jsonschema
if [ $? -ne 0 ]; then
    pip install --user jsonschema
    if [ $? -ne 0 ]; then
        echo "error: pip install failed"
        exit 1
    fi
fi

./Libraries/StyleKit/ParserJSON.py -i ${TARGET_NAME}/Style/Style.json -o ${TARGET_NAME}/Style/Style.swift

```

8. Build the project
9. Add ` Style.json ` & the generated ` Style.swift ` to the Xcode project

## Usage

Steps to add author styles and apply them to UIKit elements

1.) Your ` Style.json ` file is you single location to define the style for you application
2.) Below are examples for the currently supported features
 * Full support & validation documentation can be found in the ` Style.json.schema `

#### Fonts

```

"Fonts": {
    "fontKey": "font-bundle-identifier"
}

```

#### Font Styles

```

"fontStyle": {
    "font": "primaryFontLightItalic",
    "size": 20
}


#### Colors

```

"Colors": {
    "colorKey": {
          "red": 250,   // RGB Value between 1-255
          "green": 110, // RGB Value between 1-255
          "blue": 92,   // RGB Value between 1-255
          "alpha": 1    // Alpha Value between 0.0-1.0
    }
}

```

#### Images

```

"Images": {
    "imageKey": "image-bundle-identifier"
}

```

#### Labels

```

"Labels": {
    "H1": {
        "fontStyle": {
            "font": "primaryFontLight",
            "size": 34
        },
        "textColor": "whiteColor",
        "textAlignment": "Center"
    }
}

```

#### Buttons

To use titleColor for button state you must set the button as "Custom" type in interface builder. Currently supports button states ` normal `, ` selected `, `  highlighted `

```

"Buttons": {
  "primaryButton": {
      "fontStyle": {
          "font": "primaryFontLight", // fontKey
          "size": 34
      },
      "backgroundColor": "baseClearColor",   // colorKey
      "size": 13,
      "cornerRadius": 20,
      "borderWidth": 1,
      "borderColor": "baseBlackColor",
      "normal": {
          "titleColor": "baseBlackColor"    // colorKey
      },
      "selected": {
          "titleColor": "activityPrimaryColor",
          "backgroundColor": "baseWhiteColor"
      }
  }
}

```

#### TextFields

* textAlignment values : ` "Left", "Right", "Center", "Justified", "Natural" `
* borderStyle values : ` "None", "Line", "Bezel", "RoundedRect" `

```
"TextFields": {
        "T1": {
            "fontStyle": {
                "font": "primaryFontLight", // fontKey
                "size": 34
            },
            "textColor": "baseColorWhite", // colorKey
            "borderColor": "colorKey"      // colorKey
            "borderWidth": 1,
            "cornerRadius": 15,
            "textAlignment": "Center",
            "borderStyle": "None"
        }
    }

```

#### Xcode Integration

The output of a valid ` Style.json ` is a compiled ` Style.swift ` that file will contain ` IBOutletCollections ` & specific methods for each element defined in the ` Style.json `. These methods can be applied directly to elements via code or objects can be linked directly to a Style inside storyboards.

* To link styles in Storyboards add an object of class ` Style ` to the view / viewController you'd like to style. That will make StyleKits outlet collections available in interface builder.
* Next link the selected style outlet to it's corresponding object using the "whip tool".

## Steps to contribute

If you'd like to add support for any remaining UIKit elements follow this guide to help you through the process.

1. All new features must be validated through the ` Style.json.schema `. Documentation on json schema syntax can be found at [http://json-schema.org](http://json-schema.org).
2. Once the ` json ` structure has been defined it's properties need to be created in ` UIObjects.py `
3. If it's a UIKit element that's not already supported ` ParserJSON.py ` will need to be updated to break down the json to python objects that are feed to the swift generator.
4.) Next ` SwiftGenerator.py ` will need to updated to generate the appropriate swift code.
