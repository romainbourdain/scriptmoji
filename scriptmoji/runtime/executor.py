from scriptmoji.runtime.node import Node
from scriptmoji.lexer.lexer import Lexer
from scriptmoji.parser.yacc import Yacc
from scriptmoji.utils.cli import print_result


class Executor:
    """
    The Executor class is responsible for executing the parsed code.

    Args:
        lexer (Lexer): The lexer object used for tokenizing the code.
        yacc (Yacc): The yacc object used for parsing the code.

    Attributes:
        lexer (Lexer): The lexer object used for tokenizing the code.
        yacc (Yacc): The yacc object used for parsing the code.
    """

    def __init__(self, lexer, yacc):
        self.lexer: Lexer = lexer
        self.yacc: Yacc = yacc

    def execute(self, code):
        """
        Executes the given code.

        Args:
            code (str): The code to be executed.
        """
        ast = self.yacc.parse(code)
        result = self.run(ast)
        print_result(result)

    def run(self, node: Node) -> int:
        """
        Recursively runs the given AST node and returns the result.

        Args:
            node (Node): The AST node to be executed.

        Returns:
            The result of executing the AST node.
        """
        if node is None:
            return None

        if node.type == "operation":
            left_val = self.run(node.children[0])
            right_val = self.run(node.children[1])

            match node.operator:
                case "+":
                    return left_val + right_val
                case "-":
                    return left_val - right_val
                case "*":
                    return left_val * right_val
                case "/":
                    return left_val / right_val

        elif node.type == "number":
            return node.value

        elif node.type == "statements":
            result = None
            for child in node.children:
                result = self.run(child)
            return result

        elif node.type == "statement":
            return self.run(node.children[0])
