
def markdown_to_blocks(markdown):
    result=markdown.split("\n\n")
    for i in range(len(result)):
        if result[i]!="":
            result[i]=result[i].strip()
        else:
            result.pop(i)
    return result
