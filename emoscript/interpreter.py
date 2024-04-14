def parse(file):
    with open(file, "r") as f:
        return f.read()


def lexer(content): ...
