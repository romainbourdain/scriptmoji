from pathlib import Path
import toml


class Config:
    _config = None

    @staticmethod
    def load_config(file_path="pyproject.toml"):
        config_path = Path(file_path)
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found in {config_path}")
        with config_path.open() as f:
            Config._config = toml.load(f)
        return Config._config

    @staticmethod
    def get_config():
        if Config._config is None:
            Config.load_config()
        return Config._config
