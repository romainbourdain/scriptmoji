from runtime.node import Node
from lexer.lexer import Lexer
from parser.yacc import Yacc


class Executor:
    def __init__(self, lexer, yacc):
        self.lexer: Lexer = lexer
        self.yacc: Yacc = yacc

    def execute(self, code):
        ast = self.yacc.parse(code)
        result = self.run(ast)
        print(result)

    def run(self, node: Node):
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
