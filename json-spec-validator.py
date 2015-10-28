import sys, string

from jsonspec.validators import load

# data will validate against this schema
validator = load({
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type" : "object",
    "properties" : {
        "Fonts" : {
            "type" : "object",
            "patternProperties": {
                "^.*$" : { "$ref": "#/definitions/bundleKey" }
            }
        },
        "Colors" : {
            "type" : "object",
            "patternProperties": {
                "^.*$" : {
                    "type" : "object",
                    "pattern": "^[a-zA-Z0-9\-\_]+$",
                    "properties" : {
                        "red": { "$ref": "#/definitions/colorValue" },
                        "green": { "$ref": "#/definitions/colorValue" },
                        "blue": { "$ref": "#/definitions/colorValue" },
                        "alpha": { "$ref": "#/definitions/colorValue" }
                    },
                    "required": [ "red", "green", "blue", "alpha" ]
                }
            }
        },
        "Images" : {
            "type" : "object",
            "patternProperties": {
                "^.*$" : { "$ref": "#/definitions/bundleKey" }
            }
        },
        "Labels" : {
            "type" : "object",
            "patternProperties": {
                "^.*$" : {
                    "type" : "object",
                    "properties" : {
                        "font" : { "type" : "string" },
                        "size" : { "type" : "integer" },
                        "color" : { "type" : "string" }
                    },
                    "required": [ "font", "size" ]
                }
            }
        },
        "Buttons" : {
            "type" : "object",
            "patternProperties": {
                "^.*$" : {
                    "type" : "object",
                    "properties" : {
                        "titleLabelFont": { "type" : "string" },
                        "size": { "type" : "integer" },
                        "backgroundColor": { "type" : "string" },
                        "cornerRadius": { "type" : "integer" },
                        "normal" : { "$ref": "#/definitions/buttonState" },
                        "highlighted" : { "$ref": "#/definitions/buttonState" },
                        "selected" : { "$ref": "#/definitions/buttonState" }
                    },
                    "required": [ "titleLabelFont", "size" ]
                }
            }
        },
        "TextFields": {
            "type" : "object",
            "patternProperties": {
                "^.*$" : {
                    "type" : "object",
                    "properties" : {
                        "textColor": { "type" : "string" },
                        "backgroundColor": { "type" : "string" },
                        "borderColor": { "type" : "string" },
                        "borderWidth": { "type" : "integer" },
                        "cornerRadius": { "type" : "integer" },
                        "textAlignment": {
                            "enum": [
                                "Left",
                                "Right",
                                "Center",
                                "Justified",
                                "Natural"
                            ]
                        },
                        "borderStyle": {
                            "enum": [
                                "None",
                                "Line",
                                "Bezel",
                                "RoundedRect"
                            ]
                        }
                    }
                }
            }
        }
    },
    "definitions": {
        "bundleKey" : {
            "type" : "string",
            "pattern": "^[a-zA-Z0-9\-\_]+$"
        },
        "colorValue" : {
            "type" : "integer",
            "minimum": 0,
            "maximum": 255
        },
        "buttonState" : {
            "properties" : {
                "titleColor": {
                    "type" : "string",
                    "pattern" : "^[a-zA-Z0-9]+$"
                },
                "titleShadowColor" : {
                    "type" : "string",
                    "pattern" : "^[a-zA-Z0-9]+$"
                }
            }
        }
    }
})

# validate this data
validator.validate({
    "Fonts": {
        "fontKey": "font-bundle-identifier"
    },
    "Colors": {
        "colorKey": {
            "red": 1,
            "green": 1,
            "blue": 1,
            "alpha": 1
        }
    },
    "Images": {
        "imageKey": "image-bundle-identifier"
    },
    "Labels": {
        "LabelName": {
            "font": "fontKey",
            "size": 34,
            "textColor": "colorKey"
        }
    },
    "Buttons": {
        "ButtonName": {
            "titleLabelFont": "fontKey",
            "size": 34,
            "backgroundColor": "colorKey",
            "cornerRadius": 22,
            "normal": {
                "titleColor": "colorKey",
                "titleShadowColor" : "colorKey"
            },
            "highlighted": {
                "titleColor": "colorKey",
                "titleShadowColor" : "colorKey"
            },
            "selected": {
                "titleColor": "colorKey",
                "titleShadowColor" : "colorKey"
            }
        }
    },
    "TextFields": {
        "T1": {
            "textColor": "colorKey",
            "backgroundColor": "colorKey",
            "borderColor": "colorKey",
            "borderWidth": 1,
            "cornerRadius": 8,
            "textAlignment" : "Center",
            "borderStyle" : "None"
        }
    }
})