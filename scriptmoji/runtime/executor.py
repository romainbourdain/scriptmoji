from runtime.node import Node
from lexer.lexer import Lexer
from parser.yacc import Yacc


class Executor:
    def __init__(self, lexer, yacc):
        self.lexer: Lexer = lexer
        self.yacc: Yacc = yacc

    def run(self, code):
        ast = self.yacc.parse(code)
        result = self.execute(ast)
        print(result)

    def execute(self, node: Node):
        if node is None:
            return None
        if node.type == "operation":
            left_val = self.execute(node.left)
            right_val = self.execute(node.right)

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
