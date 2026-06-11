from textnode import TextNode, TextType




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



