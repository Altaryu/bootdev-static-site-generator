import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_neq(self):
        node = HTMLNode("p", "This is a paragraph", None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertNotEqual(node.props_to_html(), ' class="greeting" href="https://boot.dev"')

if __name__ == "__main__":
    unittest.main()