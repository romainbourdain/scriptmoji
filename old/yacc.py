import ply.yacc as yacc


class Yacc:
    def __init__(self, lexer) -> None:
        self.tokens = lexer.tokens
        self.lexer = lexer
        self.parser = yacc.yacc(module=self)

    def p_expression_plus(self, p):
        "expression : expression PLUS term"
        p[0] = p[1] + p[3]

    def p_expression_minus(self, p):
        "expression : expression MINUS term"
        p[0] = p[1] - p[3]

    def p_expression_term(self, p):
        "expression : term"
        p[0] = p[1]

    def p_term_times(self, p):
        "term : term TIMES factor"
        p[0] = p[1] * p[3]

    def p_term_divide(self, p):
        "term : term DIVIDE factor"
        p[0] = p[1] / p[3]

    def p_term_factor(self, p):
        "term : factor"
        p[0] = p[1]

    def p_factor_number(self, p):
        "factor : NUMBER"
        p[0] = p[1]

    def p_factor_expression(self, p):
        "factor : LPAREN expression RPAREN"
        p[0] = p[2]

    def p_error(self, p):
        print(f"Syntax error at {p.value}")

    def parse(self, data):
        return self.parser.parse(data, lexer=self.lexer.lexer)
