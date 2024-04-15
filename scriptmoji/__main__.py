from lexer.lexer import Lexer
from parser.yacc import Yacc
from runtime.executor import Executor
from utils.config import Config
from cli.argparser import ArgParser
from cli.shell import Shell


def main():
    Config.load_config("pyproject.toml")

    lexer = Lexer()
    parser = Yacc(lexer)
    executor = Executor(lexer, parser)

    arg_parser = ArgParser()
    args = arg_parser.parse_args()

    if args.file:
        with open(args.file, "r") as file:
            script = file.read()
        result = executor.execute(script)
        print("Result:", result)

    else:
        shell = Shell(lexer, parser)
        shell.run()


if __name__ == "__main__":
    main()
