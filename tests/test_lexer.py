import pytest
from scriptmoji.lexer.lexer import Lexer


@pytest.fixture
def lexer():
    return Lexer()


def test_number(lexer):
    lexer.input("1️⃣2️⃣3️⃣")
    token = lexer.token()
    assert token.type == "NUMBER"
    assert token.value == 123


def test_operator(lexer):
    operators = {"🙂": "PLUS", "🙁": "MINUS", "😁": "TIMES", "😫": "DIVIDE"}
    for op, expected in operators.items():
        lexer.input(op)
        token = lexer.token()
        assert token.type == expected, f"Expected {expected} for '{op}'"


def test_parentheses(lexer):
    lexer.input("🫷🫸")
    token = lexer.token()
    assert token.type == "LPAREN"
    token = lexer.token()
    assert token.type == "RPAREN"


def test_whitespace(lexer):
    lexer.input("  \t  \t")
    token = lexer.token()
    assert token is None, "Lexer should ignore white spaces"
