from textnode import TextNode, TextType

def main():
    t = TextNode("Hello", TextType.BOLD, "https://www.google.com")
    print(t)



if __name__ == "__main__":
    main()