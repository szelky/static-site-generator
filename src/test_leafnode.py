import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "This is a raw text.")
        self.assertEqual(node.to_html(), "This is a raw text.")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Google", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Google</a>')

if __name__ == '__main__':
    unittest.main()
