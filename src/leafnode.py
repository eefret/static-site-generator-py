from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(value=value, tag=tag, props=props, children=None)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag is None:
            return self.value
        space = "" if self.props is None or len(self.props) == 0 else " "
        return f"<{self.tag}{space}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props})"