from enum import Enum
from htmlnode import HTMLNode, ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from extract_markdown_images import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_html_node(markdown):
    children=[]
    blocks=markdown_to_blocks(markdown)
    for block in blocks:
        html_node=block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    blocktype=block_to_block_type(block)
    if blocktype==BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if blocktype==BlockType.HEADING:
        return heading_to_html_node(block)
    if blocktype==BlockType.CODE:
        return code_to_html_node(block)
    if blocktype==BlockType.QUOTE:
        return quote_to_html_node(block)
    if blocktype==BlockType.UNORDERED_LIST:
        return ulist_to_html_node(block)
    if blocktype==BlockType.ORDERED_LIST:
        return olist_to_html_node(block)
    raise ValueError("invalid block type")

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def text_to_children(text):
    text_nodes=text_to_textnodes(text)
    children=[]
    for text_node in text_nodes:
        html_node=text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level=0
    for char in block:
        if char == '#':
            level+=1
        else:
            break
    if level > 6:
        raise ValueError("invalid heading level")
    else:
        text = block[level + 1 :]
        children=text_to_children(text)
        return ParentNode(f"h{level}", children)
    
def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("not valid code syntax")
    else:
        text=block[4 : -3]
        raw_text_node=TextNode(text, TextType.TEXT)
        child=text_node_to_html_node(raw_text_node)
        code=ParentNode("code", [child])
        return ParentNode("pre", [code])
    
def olist_to_html_node(block):
    lines=block.split("\n")
    items=[]
    for item in items:
        split=item.split(". ", 1)
        text=split[1]
        children=text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)

def ulist_to_html_node(block):
    lines=block.split("\n")
    items=[]
    for item in items:
        text=item[2:]
        children=text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)


def markdown_to_blocks(markdown):
    result=markdown.split("\n\n")
    for i in range(len(result)):
        if result[i]!="":
            result[i]=result[i].strip()
        else:
            result.pop(i)
    return result

def block_to_block_type(markdown):
    if "# " in markdown or "## " in markdown or "### " in markdown or "#### " in markdown or "##### " in markdown or "###### " in markdown:
        return BlockType.HEADING
    elif "```\n" in markdown:
        return BlockType.CODE
    elif ">" in markdown and "<" in markdown:
        return BlockType.QUOTE
    elif "- " in markdown:
        return BlockType.UNORDERED_LIST
    elif "1. " in markdown:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
