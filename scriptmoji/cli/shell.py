from scriptmoji.utils.cli import *
from scriptmoji.runtime.executor import Executor
from scriptmoji.utils.cli import prompt_input


class Shell:
    """
    Represents a command-line shell for executing commands.

    Args:
        lexer: The lexer object used for tokenizing input commands.
        yacc: The yacc object used for parsing input commands.
    """

    def __init__(self, lexer, yacc):
        self.lexer = lexer
        self.yacc = yacc
        self.executor = Executor(lexer, yacc)

    def run(self):
        """
        Runs the shell and prompts for user input.

        The shell will continue running until the user enters the "exit" command.
        """
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
