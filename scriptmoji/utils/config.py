from pathlib import Path
import toml


class Config:
    """
    A class for managing configuration settings.

    This class provides methods to load and retrieve configuration settings from a TOML file.
    """

    _config: dict = None

    @staticmethod
    def load_config(file_path: str = "pyproject.toml") -> dict:
        """
        Load the configuration from a TOML file.

        Args:
            file_path (str, optional): The path to the TOML file. Defaults to "pyproject.toml".

        Returns:
            dict: The loaded configuration as a dictionary.

        Raises:
            FileNotFoundError: If the specified config file is not found.
        """

        config_path = Path(file_path)
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found in {config_path}")
        with config_path.open() as f:
            Config._config = toml.load(f)
        return Config._config

    @staticmethod
    def get_config() -> dict:
        """
        Retrieve the configuration dictionary.

        If the configuration has not been loaded yet, this function will load it before returning.

        Returns:
            dict: The configuration dictionary.
        """
        if Config._config is None:
            Config.load_config()
        return Config._config
