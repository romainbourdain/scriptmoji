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


def print_error(message, code=1):
    config = Config.get_config()
    error_prefix = config["tool"]["shell"]["error_prefix"]
    print(f"{error_prefix} {message}")
    sys.exit(code)


def print_debug(message):
    config = Config.get_config()
    print(f"{message}")
