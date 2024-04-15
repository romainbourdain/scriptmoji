from utils.cli import *
from runtime.executor import Executor
from utils.cli import prompt_input


class Shell:
    def __init__(self, lexer, yacc):
        self.lexer = lexer
        self.yacc = yacc
        self.executor = Executor(lexer, yacc)

    def run(self):
        print_welcome()
        while True:
            try:
                command = prompt_input()
                if command.lower() == "exit":
                    print_exit()
                    break

                if command.strip():
                    self.executor.execute(command)

            except Exception as e:
                print_error(str(e))
