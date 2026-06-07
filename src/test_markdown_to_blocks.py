import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type

def test_markdown_to_blocks(self):
    md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
        )
    
def test_block_to_block_type_equal(self):
        block = block_to_block_type("This is a paragraph")
        block2 = block_to_block_type("This is also a paragraph")
        self.assertEqual(block, block2)

def test_block_to_block_type_inequal(self):
        block = block_to_block_type("This is a paragraph")
        block2 = block_to_block_type("# This is a heading")
        self.assertNotEqual(block, block2)

if __name__ == "__main__":
    unittest.main()