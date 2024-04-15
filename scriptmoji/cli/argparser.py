from argparse import ArgumentParser, Namespace
from pathlib import Path
from utils.config import Config


class ArgParser(ArgumentParser):
    def __init__(self, config_path="pyproject.toml"):
        super().__init__()
        self.config = Config.load_config(config_path)["tool"]["poetry"]
        self.description = self.config["description"]
        self.version = self.config["version"]
        self.prog = self.config["name"]
        self.define_arguments()

    def define_arguments(self):
        self.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"💪 {self.version}",
        )
        self.add_argument("-f", "--file", help="ScriptMoji file to execute", type=str)

    def parse_args(self, *args, **kwargs) -> Namespace:
        args = super().parse_args(*args, **kwargs)
        if args.file and not Path(args.file).exists():
            raise FileNotFoundError(f"File not found: {args.file}")
        return args
