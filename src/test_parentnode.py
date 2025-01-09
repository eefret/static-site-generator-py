import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    
    def test_to_html_success(self):
        node = ParentNode(tag="div", children=[ParentNode(tag="p", children=[LeafNode(tag="a", value="this is a link", props={"href": "https://www.google.com"})])])
        self.assertEqual(node.to_html(), '<div><p><a href="https://www.google.com">this is a link</a></p></div>')
        
    def test_to_html_fail(self):
        node = ParentNode(tag="div", children=None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode children cannot be None")
    
    def test_repr(self):
        node = ParentNode(tag="div", children=[ParentNode(tag="p", children=[LeafNode(tag="a", value="this is a link", props={"href": "https://www.google.com"})])])
        self.assertEqual(repr(node), "ParentNode(div, None, [ParentNode(p, None, [LeafNode(a, this is a link, None, {'href': 'https://www.google.com'})], None)], None)")
        
    def test_to_html_fail_tag_none(self):
        node = ParentNode(tag=None, children=[ParentNode(tag="p", children=[LeafNode(tag="a", value="this is a link", props={"href": "https://www.google.com"})])])
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode tag cannot be None")
        
    def test_no_space_after_tag_on_starting_tag(self):
        node = ParentNode(tag="div", children=[ParentNode(tag="p", children=[LeafNode(tag="a", value="this is a link", props={"href": "https://www.google.com"})])])
        self.assertEqual(node.to_html(), '<div><p><a href="https://www.google.com">this is a link</a></p></div>')

if __name__ == "__main__":
    unittest.main()