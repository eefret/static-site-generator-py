import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_success(self):
        node = HTMLNode(tag="a", value="this is a link", props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com"')
        
    def test_props_to_html_fail(self):
        node = HTMLNode(tag="a", value="this is a link")
        self.assertEqual(node.props_to_html(), "")
    
    def test_repr(self):
        node = HTMLNode(tag="a", value="this is a link", props={"href": "https://www.google.com"})
        self.assertEqual(repr(node), "HTMLNode(a, this is a link, None, {'href': 'https://www.google.com'})")
        

if __name__ == "__main__":
    unittest.main()