import ply.yacc as yacc
from scriptmoji.runtime.node import Node
from scriptmoji.utils.cli import print_error
from scriptmoji.utils.emoji import emoji_to_operator


class Yacc:
    """
    Yacc class represents a parser generator.

    Args:
        lexer: The lexer object used for tokenizing input.

    Attributes:
        tokens (list): The list of tokens defined in the lexer.
        lexer: The lexer object used for tokenizing input.
        parser: The parser object generated by yacc.

    """

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
            p[0] = Node(
                type="operation",
                children=[p[1], p[3]],
                operator=emoji_to_operator(p[2]),
            )
        else:
            p[0] = p[1]

    def p_term(self, p: yacc.YaccProduction):
        """
        term : term TIMES factor
             | term DIVIDE factor
             | factor
        """
        if len(p) == 4:
            p[0] = Node(
                type="operation",
                children=[p[1], p[3]],
                operator=emoji_to_operator(p[2]),
            )
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
        """
        Parse the input data using the generated parser.

        Args:
            data (str): The input data to be parsed.

        Returns:
            Node: The root node of the parsed abstract syntax tree.

        """
        return self.parser.parse(data, lexer=self.lexer.lexer)
