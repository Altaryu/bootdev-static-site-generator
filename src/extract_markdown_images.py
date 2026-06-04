import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    matches=re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches=re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes=[]
    for node in old_nodes:
        image_matches=extract_markdown_images(node.text)
        if image_matches!=[]:
            for match in image_matches:
                sections=node.text.split(f"![{match[0]}]({match[1]})")
                for i in range(len(sections)):
                    if i % 2 == 0:
                        new_nodes.append(TextNode(sections[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes=[]
    for node in old_nodes:
        link_matches=extract_markdown_links(node.text)
        if link_matches!=[]:
            for match in link_matches:
                sections=node.text.split(f"![{match[0]}]({match[1]})")
                for i in range(len(sections)):
                    if i % 2 == 0:
                        new_nodes.append(TextNode(sections[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
    return new_nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]
    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            new_nodes.append(node)
        else:
            if delimiter!='**' and delimiter!='_' and delimiter!='`':
                raise Exception("invalid delimiter")
            else:
                split_nodes=[]
                split=node.text.split(delimiter)
                for s in range(len(split)):
                    if s % 2 == 0:
                        split_nodes.append(TextNode(split[s], TextType.TEXT))
                    else:
                        if delimiter=='**':
                            split_nodes.append(TextNode(split[s], TextType.BOLD))
                        elif delimiter=='_':
                            split_nodes.append(TextNode(split[s], TextType.ITALIC))
                        elif delimiter=='`':
                            split_nodes.append(TextNode(split[s], TextType.BOLD))
                new_nodes.extend(split_nodes)
    return new_nodes