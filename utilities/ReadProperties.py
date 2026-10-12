import os
import configparser


class ReadConfig:

    config = configparser.ConfigParser()
    _config_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "Configurations", "config.ini")
    )
    config.read(_config_path)

    @staticmethod
    def get_base_url():
        return ReadConfig.config.get("common", "base_url")

    @staticmethod
    def get_browser():
        return ReadConfig.config.get("common", "browser")