import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        new_node = []
        section = node.text.split(delimiter)
        if len(section) % 2 == 0:
            raise Exception("invalid markdown syntax no closing delimiter")
        for i in range(len(section)):
            if section[i] == "":
                continue
            if i % 2 == 0:
                new_node.append(TextNode(section[i], TextType.TEXT))
            else:
                new_node.append(TextNode(section[i], text_type))
        new_nodes.extend(new_node)
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        image = extract_markdown_images(node.text)
        if not image:
            new_nodes.append(node)
            continue
        new_node = []
        section = node.text.split(f"![{image[0][0]}]({image[0][1]})")
        new_node.append(TextNode(section[0], TextType.TEXT))
        new_node.append(TextNode(image[0][0], TextType.IMAGE, image[0][1]))
        new_nodes.extend(new_node)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        link = extract_markdown_links(node.text)
        if not link:
            new_nodes.append(node)
            continue
    return new_nodes

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text: str) -> list[tuple]:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

