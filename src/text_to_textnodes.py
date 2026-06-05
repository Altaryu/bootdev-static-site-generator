from split_nodes_delimiter import split_nodes_delimiter
from extract_markdown_images import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
    initial_node=[TextNode(text, TextType.TEXT)]
    result=split_nodes_delimiter(initial_node, "**", TextType.BOLD)
    result=split_nodes_delimiter(result, "_", TextType.ITALIC)
    result=split_nodes_delimiter(result, "`", TextType.CODE)
    result=split_nodes_image(result)
    result=split_nodes_link(result)
    return result