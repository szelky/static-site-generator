class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented")

    def props_to_html(self):
        prop = ""
        if self.props:
            for k, v in self.props.items():
                prop += f' {k}="{v}"'
        return prop

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list["HTMLNode"], props: dict[str, str] | None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        self.child = ""
        if not self.tag:
            raise ValueError("All parent nodes must have a tag.")
        if not self.children:
            raise ValueError("All parent nodes must have children.")
        for child in self.children:
            self.child += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{self.child}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

