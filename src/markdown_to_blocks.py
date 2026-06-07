from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

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
