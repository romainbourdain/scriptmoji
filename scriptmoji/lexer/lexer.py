import ply.lex as lex


class Lexer(object):
    tokens = (
        "NUMBER",  # les nombres (en hexadécimal)
        "PLUS",  # pour les opérations +
        "MINUS",  # pour les opérations -
        "TIMES",  # pour les opérations *
        "DIVIDE",  # pour les opérations /
        "LPAREN",  # pour (
        "RPAREN",  # pour )
    )

    t_PLUS = r"\+"
    t_MINUS = r"-"
    t_TIMES = r"\*"
    t_DIVIDE = r"/"
    t_LPAREN = r"\("
    t_RPAREN = r"\)"

    def t_NUMBER(self, t):
        r"\d+"
        t.value = int(t.value)
        return t

    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    t_ignore = " \t"

    def t_error(self, t):
        print(f"Illegal character {t.value[0]}")
        t.lexer.skip(1)

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def input(self, data):
        self.lexer.input(data)

    def token(self):
        return self.lexer.token()
