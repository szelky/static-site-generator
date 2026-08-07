import os
import shutil
from generate_page import generate_page

static_path = "./static"
public_path = "./public"
content_path = "./content"
template = "./template.html"

def main() -> None:
    print("Deleting public directory...")
    if "public" in os.listdir("."):
        shutil.rmtree("./public")

    print("Copying static files to public directory...")
    copy_static_to_public(static_path, public_path)

    print("Generating Page...")
    generate_page(
        os.path.join(content_path, "index.md"),
        template,
        os.path.join(public_path, "index.html")
    )

def copy_static_to_public(src: str, dst: str) -> None:
    ls_src = os.listdir(src)
    if not os.path.exists(dst):
        os.mkdir(dst)
    for item in ls_src:
        path_src = os.path.join(src, item)
        path_dst = os.path.join(dst, item)
        print(f" * {path_src} -> {path_dst}")
        if os.path.isfile(path_src):
            shutil.copy(path_src, path_dst)
        else:
            copy_static_to_public(path_src, path_dst)

main()
