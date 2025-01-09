from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    STRIKETHROUGH = "strikethrough"
    CODE = "code"
    TEXT = "text"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url :str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, tn):
        return self.text == tn.text and self.text_type == tn.text_type and self.url == tn.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.UNDERLINE:
            return LeafNode(tag="u", value=text_node.text)
        case TextType.STRIKETHROUGH:
            return LeafNode(tag="s", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("Invalid TextType")