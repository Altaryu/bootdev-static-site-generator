from textnode import TextNode
import os
import shutil
print("hello world")

def copy_content(source, destination):
    if os.path.exists(source):
        if not os.path.exists(destination):
            os.mkdir(destination)
        
        for item in os.listdir(source):
            if os.path.isfile(os.path.join(source, item)):
                print(f"File: {os.path.join(source, item)}")
                shutil.copy(os.path.join(source, item), destination)
                #files.append(os.path.join(source, item))
            else:
                print(f"Subdirectory: {os.path.join(source, item)}")
                copy_content(os.path.join(source, item), os.path.join(destination, item))
                #dirs.append(os.path.join(source, item))

    
def main():
    shutil.rmtree("public")
    copy_content("static", "public")
    tn=TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(tn)

main()