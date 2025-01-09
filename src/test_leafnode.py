import unittest 
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_success(self):
        node = LeafNode(tag="a", value="this is a link", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">this is a link</a>')
        
    def test_to_html_fail(self):
        node = LeafNode(tag="a", value=None)
        with self.assertRaises(ValueError):
            node.to_html()
        
    def test_repr(self):
        node = LeafNode(tag="a", value="this is a link", props={"href": "https://www.google.com"})
        self.assertEqual(repr(node), "LeafNode(a, this is a link, None, {'href': 'https://www.google.com'})")

if __name__ == "__main__":
    unittest.main()