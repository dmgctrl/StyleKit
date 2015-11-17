from jsonschema import validators

class Validator:

    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "Fonts": {
                "type": "object",
                "patternProperties": {
                    "^.*$": {"$ref": "#/definitions/bundleKey"}
                }
            },
            "Colors": {
                "type": "object",
                "patternProperties": {
                    "^.*$": {
                        "type": "object",
                        "pattern": "^[a-zA-Z0-9\-\_]+$",
                        "properties": {
                            "red": {"$ref": "#/definitions/colorValue"},
                            "green": {"$ref": "#/definitions/colorValue"},
                            "blue": {"$ref": "#/definitions/colorValue"},
                            "alpha": {"$ref": "#/definitions/alphaValue"}
                        },
                        "required": ["red", "green", "blue", "alpha"]
                    }
                }
            },
            "Images": {
                "type": "object",
                "patternProperties": {
                    "^.*$": {"$ref": "#/definitions/bundleKey"}
                }
            },
            "Labels": {
                "type": "object",
                "patternProperties": {
                    "^.*$": {
                        "type": "object",
                        "properties": {
                            "font": {"type": "string"},
                            "size": {"type": "integer"},
                            "color": {"type": "string"}
                        },
                        "required": ["font", "size"]
                    }
                }
            },
            "Buttons": {
                "type": "object",
                "patternProperties": {
                    "^.*$": {
                        "type": "object",
                        "properties": {
                            "titleLabelFont": {"type": "string"},
                            "size": {"type": "integer"},
                            "backgroundColor": {"type": "string"},
                            "cornerRadius": {"type": "integer"},
                            "normal": {"$ref": "#/definitions/buttonState"},
                            "highlighted": {"$ref": "#/definitions/buttonState"},
                            "selected": {"$ref": "#/definitions/buttonState"}
                        },
                        "required": ["titleLabelFont", "size"]
                    }
                }
            },
            "TextFields": {
                "type": "object",
                "patternProperties": {
                    "^.*$": {
                        "type": "object",
                        "properties": {
                            "attributes": {"type": "object"},
                            "textcolor": {"type": "string"},
                            "backgroundColor": {"type": "string"},
                            "borderColor": {"type": "string"},
                            "borderWidth": {"type": "integer"},
                            "cornerRadius": {"type": "integer"},
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
            "bundleKey": {
                "type": "string",
                "pattern": "^[a-zA-Z0-9\-\_]+$"
            },
            "colorValue": {
                "type": "integer",
                "minimum": 0,
                "maximum": 255
            },
            "alphaValue": {
                "type": "number",
                "minimum": 0.0,
                "maximum": 1.0
            },
            "buttonState": {
                "properties": {
                    "titleColor": {
                        "type": "string",
                        "pattern": "^[a-zA-Z0-9]+$"
                    },
                    "titleShadowColor": {
                        "type": "string",
                        "pattern": "^[a-zA-Z0-9]+$"
                    }
                }
            }
        }
    }

    def validate(self, style):
        validators.validate(style, Validator.schema)
