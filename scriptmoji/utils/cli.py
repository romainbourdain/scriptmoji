from utils.config import Config
import sys


def print_welcome():
    config = Config.get_config()
    welcome_message = config["tool"]["shell"]["welcome_message"]
    print(welcome_message)


def print_exit():
    config = Config.get_config()
    exit_message = config["tool"]["shell"]["exit_message"]
    print(exit_message)


def prompt_input():
    config = Config.get_config()
    prompt_prefix = config["tool"]["shell"]["prompt_prefix"]
    return input(f"{prompt_prefix} ")


def print_result(result: str):
    config = Config.get_config()
    result_prefix = config["tool"]["shell"]["result_prefix"]
    print(f"{result_prefix} {result}")


def print_error(message: str, code: int = 1):
    config = Config.get_config()
    error_prefix = config["tool"]["shell"]["error_prefix"]
    print(f"{error_prefix} {message}")
    sys.exit(code)
