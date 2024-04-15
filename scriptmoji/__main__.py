from lexer.lexer import Lexer
from parser.yacc import Yacc
from runtime.executor import Executor
from utils.config import Config
from cli.argparser import ArgParser
from cli.shell import Shell
from typing import NoReturn


def main() -> NoReturn:
    """
    Entry point of the scriptmoji application.

    This function loads the configuration, initializes the lexer, parser, and executor,
    parses the command-line arguments, and either executes a script file or starts the interactive shell.
    """

    Config.load_config("pyproject.toml")

    lexer = Lexer()
    parser = Yacc(lexer)
    executor = Executor(lexer, parser)

    arg_parser = ArgParser()
    args = arg_parser.parse_args()

    if args.file:
        with open(args.file, "r") as file:
            script = file.read()
        executor.execute(script)

    else:
        shell = Shell(lexer, parser)
        shell.run()


if __name__ == "__main__":
    main()
