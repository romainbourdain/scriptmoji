from typing import List


class Node:
    """
    Represents a node in a tree structure.

    Attributes:
        type (str): The type of the node.
        value (int): The value associated with the node.
        children (List[Node]): The child nodes of the current node.
        operator (str): The operator associated with the node.
    """

    def __init__(
        self,
        type: str,
        value: int = None,
        children: List["Node"] = [],
        operator: str = None,
    ):
        self.type = type
        self.children = children
        self.value = value
        self.operator = operator
