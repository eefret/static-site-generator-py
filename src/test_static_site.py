import unittest
from static_site import extract_title

class TestStaticSiteGenerator(unittest.TestCase):
    def test_extract_title_basic(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")
    
    def test_extract_title_with_extra_whitespace(self):
        markdown = "#    Spaced    Title    "
        self.assertEqual(extract_title(markdown), "Spaced    Title")
    
    def test_extract_title_multiline(self):
        markdown = """
Some text here
# The Real Title
## Subtitle
        """
        self.assertEqual(extract_title(markdown), "The Real Title")
    
    def test_extract_title_no_h1(self):
        markdown = "## Not an h1\nJust some text"
        with self.assertRaises(ValueError):
            extract_title(markdown)
    
    def test_extract_title_empty(self):
        with self.assertRaises(ValueError):
            extract_title("")