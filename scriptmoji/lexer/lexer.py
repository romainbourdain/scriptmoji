import ply.lex as lex
from scriptmoji.utils.cli import print_error
from scriptmoji.utils.emoji import emoji_to_number


class Lexer(object):
    """
    The Lexer class is responsible for tokenizing input data into a sequence of tokens.

    Attributes:
        tokens (tuple): A tuple of token names.
    """

    tokens = (
        "NUMBER",
        "PLUS",
        "MINUS",
        "TIMES",
        "DIVIDE",
        "LPAREN",
        "RPAREN",
        "NEWLINE",
    )

    t_PLUS = r"🙂"
    t_MINUS = r"🙁"
    t_TIMES = r"😁"
    t_DIVIDE = r"😫"
    t_LPAREN = r"🫷"
    t_RPAREN = r"🫸"

    def t_NUMBER(self, t):
        r"[0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣]+"
        t.value = emoji_to_number(t.value)
        return t

    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)
        t.type = "NEWLINE"
        return t

    t_ignore = " \t"

    def t_error(self, t):
        print_error(f"Illegal character {t.value[0]}")
        t.lexer.skip(1)

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def input(self, data):
        """
        Sets the input data for the lexer.

        Parameters:
        - data: The input data to be processed by the lexer.
        """
        self.lexer.input(data)

    def token(self):
        """
        Retrieves the next token from the lexer.

        Returns:
            The next token from the lexer.
        """
        return self.lexer.token()
