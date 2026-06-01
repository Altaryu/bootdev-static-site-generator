import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert_nodes=[TextNode("This is text with a ", TextType.TEXT, None),
                      TextNode("code block", TextType.CODE, None),
                      TextNode(" word", TextType.TEXT, None)]
        self.assertEqual(new_nodes, assert_nodes)

    def test_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        assert_nodes=[TextNode("This is text with an ", TextType.TEXT, None),
                      TextNode("italic", TextType.ITALIC, None),
                      TextNode(" word", TextType.TEXT, None)]
        self.assertEqual(new_nodes, assert_nodes)
    
    def test_code(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert_nodes=[TextNode("This is text with a ", TextType.TEXT, None),
                      TextNode("bold", TextType.BOLD, None),
                      TextNode(" word", TextType.TEXT, None)]
        self.assertEqual(new_nodes, assert_nodes)


if __name__ == "__main__":
    unittest.main()