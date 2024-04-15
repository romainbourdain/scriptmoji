from argparse import ArgumentParser
from pathlib import Path
import toml


class ArgParser(ArgumentParser):
    def __init__(self):
        self.load_config()
        super().__init__(
            prog=self.config["name"], description=self.config["description"]
        )
        self.create_arguments()

    def load_config(self):
        config_path = Path("pyproject.toml")
        if not config_path.exists():
            raise FileNotFoundError(f"Config not found in {config_path}")

        with open(config_path) as f:
            toml_data = toml.load(f)

        self.config = toml_data["project"]

    def create_arguments(self):
        self.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"%(prog)s {self.config['version']}",
        )
        self.add_argument(
            "-i",
            "--input",
            help="File to read",
            default="",
            type=str,
            action="store",
        )

    def parse_args(self):
        args = super().parse_args()

        target_dir = Path(args.input)
        if not target_dir.exists():
            raise FileNotFoundError(f"File {target_dir} not found")

        return args
