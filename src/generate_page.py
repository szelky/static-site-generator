import os
from block_markdown import markdown_to_html_node

def extract_title(markdown: str) -> str:
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("no title found")

def generate_page(src: str, tmp: str, dst: str) -> None:
    print(f" * {src} {tmp} -> {dst}")
    with open(src) as file:
        md_src = file.read()

    title = extract_title(md_src)
    content = markdown_to_html_node(md_src).to_html()

    with open(tmp) as file:
        md_tmp = file.read()
        md_tmp = md_tmp.replace("{{ Title }}", title)
        md_tmp = md_tmp.replace("{{ Content }}", content)
    with open(dst, "w") as file:
        file.write(md_tmp)

def generate_pages_recursive(src: str, tmp: str, dst: str):
    pass
