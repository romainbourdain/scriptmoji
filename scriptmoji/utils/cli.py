from utils.config import Config
import sys


def print_welcome():
    """
    Prints the welcome message defined in the configuration file.
    """
    config = Config.get_config()
    welcome_message = config["tool"]["shell"]["welcome_message"]
    print(welcome_message)


def print_exit():
    """
    Prints the exit message defined in the configuration file.
    """
    config = Config.get_config()
    exit_message = config["tool"]["shell"]["exit_message"]
    print(exit_message)


def prompt_input():
    """
    Prompts the user for input and returns the input value.
    Use the prompt_prefix from the configuration file.

    Returns:
        str: The user input value.
    """
    config = Config.get_config()
    prompt_prefix = config["tool"]["shell"]["prompt_prefix"]
    return input(f"{prompt_prefix} ")


def print_result(result: str):
    """
    Prints the result of a prompt.
    Use the result_prefix from the configuration file.

    Args:
        result (str): The result to be printed.
    """
    config = Config.get_config()
    result_prefix = config["tool"]["shell"]["result_prefix"]
    print(f"{result_prefix} {result}")


import sys


def print_error(message: str, code: int = 1):
    """
    Prints an error message with a specified code and exits the program.
    Use the error_prefix from the configuration file.

    Args:
        message (str): The error message to be printed.
        code (int, optional): The exit code to be used. Defaults to 1.
    """
    config = Config.get_config()
    error_prefix = config["tool"]["shell"]["error_prefix"]
    print(f"{error_prefix} {message}")
    sys.exit(code)
