from textnode import TextNode, TextType

def main() -> None:
    obj = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(obj)

main()
