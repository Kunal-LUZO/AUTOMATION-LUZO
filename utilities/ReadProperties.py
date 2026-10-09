import configparser


class ReadConfig:

    config = configparser.ConfigParser()
    config.read("./Configurations/config.ini")

    @staticmethod
    def get_base_url():
        return ReadConfig.config.get("common", "base_url")

    @staticmethod
    def get_browser():
        return ReadConfig.config.get("common", "browser")