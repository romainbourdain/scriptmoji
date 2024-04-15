class Node:
    def __init__(self, type, value=None, children=[], operator=None):
        self.type = type
        self.children = children
        self.value = value
        self.operator = operator
