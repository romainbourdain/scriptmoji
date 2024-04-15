import ply.yacc as yacc
from runtime.node import Node


class Yacc:
    def __init__(self, lexer):
        self.tokens = lexer.tokens
        self.lexer = lexer
        self.parser = yacc.yacc(module=self)

    def p_statement(self, p):
        """
        statements : statements statement
                | statement
        """
        if len(p) == 3:
            p[0] = Node(type="statements", children=p[1].children + [p[2]])
        else:
            p[0] = Node(type="statements", children=[p[1]])

    def p_statement_expression(self, p):
        """
        statement : expression NEWLINE
                | expression
        """
        p[0] = Node(type="statement", children=[p[1]])

    def p_expression_plus(self, p):
        "expression : expression PLUS term"
        p[0] = Node(type="operation", children=[p[1], p[3]], operator="+")

    def p_expression_minus(self, p):
        "expression : expression MINUS term"
        p[0] = Node(type="operation", children=[p[1], p[3]], operator="-")

    def p_expression_term(self, p):
        "expression : term"
        p[0] = p[1]

    def p_term_times(self, p):
        "term : term TIMES factor"
        p[0] = Node(type="operation", children=[p[1], p[3]], operator="*")

    def p_term_divide(self, p):
        "term : term DIVIDE factor"
        p[0] = Node(type="operation", children=[p[1], p[3]], operator="/")

    def p_term_factor(self, p):
        "term : factor"
        p[0] = p[1]

    def p_factor_number(self, p):
        "factor : NUMBER"
        p[0] = Node(type="number", value=p[1])

    def p_expression_parenthesis(self, p):
        "factor : LPAREN expression RPAREN"
        p[0] = p[2]

    def p_error(self, p):
        print(f"Syntax error in input! ${p}")

    def parse(self, data) -> Node:
        return self.parser.parse(data, lexer=self.lexer.lexer)
