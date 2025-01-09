from enum import Enum

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    STRIKETHROUGH = "strikethrough"
    CODE = "code"
    TEXT = "text"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url :str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, tn):
        return self.text == tn.text and self.text_type == tn.text_type and self.url == tn.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"