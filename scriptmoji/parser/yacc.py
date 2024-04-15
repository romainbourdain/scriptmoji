import ply.yacc as yacc
from runtime.node import Node
from utils.cli import print_error


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

    def p_expression(self, p):
        """
        expression : expression PLUS expression
                | expression MINUS expression
                | term
        """
        if len(p) == 4:
            p[0] = Node(type="operation", children=[p[1], p[3]], operator=p[2])
        else:
            p[0] = p[1]

    def p_term(self, p):
        """
        term : term TIMES factor
            | term DIVIDE factor
            | factor
        """
        if len(p) == 4:
            p[0] = Node(type="operation", children=[p[1], p[3]], operator=p[2])
        else:
            p[0] = p[1]

    def p_factor(self, p):
        """
        factor : NUMBER
            | LPAREN expression RPAREN
        """
        if len(p) == 2:
            p[0] = Node(type="number", value=p[1])
        else:
            p[0] = p[2]

    def p_error(self, p):
        print_error(f"Syntax error in input! ${p}")

    def parse(self, data) -> Node:
        return self.parser.parse(data, lexer=self.lexer.lexer)
