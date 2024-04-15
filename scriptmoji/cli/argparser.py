from argparse import ArgumentParser, Namespace
from pathlib import Path
from scriptmoji.utils.config import Config


class ArgParser(ArgumentParser):
    """
    Custom argument parser for ScriptMoji.

    Args:
        config_path (str): Path to the configuration file (default: "pyproject.toml")
    """

    def __init__(self, config_path: str = "pyproject.toml"):
        super().__init__()
        self.config = Config.load_config(config_path)["tool"]["poetry"]
        self.description = self.config["description"]
        self.version = self.config["version"]
        self.prog = self.config["name"]
        self.define_arguments()

    def define_arguments(self):
        """
        Define the command-line arguments for ScriptMoji.
        """
        self.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"💪 {self.version}",
        )
        self.add_argument("-f", "--file", help="ScriptMoji file to execute", type=str)

    def parse_args(self, *args, **kwargs) -> Namespace:
        """
        Parse the command-line arguments and return the parsed arguments.

        Returns:
            Namespace: Parsed command-line arguments
        """
        args = super().parse_args(*args, **kwargs)
        if args.file and not Path(args.file).exists():
            raise FileNotFoundError(f"File not found: {args.file}")
        return args
