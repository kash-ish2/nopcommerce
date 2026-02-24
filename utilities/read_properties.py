import configparser
import os

config = configparser.ConfigParser()

# Get absolute path of config.ini
current_file = os.path.abspath(__file__)
utilities_folder = os.path.dirname(current_file)
project_root = os.path.dirname(utilities_folder)

config_path = os.path.join(project_root, "configuration", "config.ini")

print("CONFIG PATH:", config_path)
print("FILE EXISTS:", os.path.exists(config_path))

config.read(config_path)

print("SECTIONS FOUND:", config.sections())


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        return config.get("admin login info", "admin_page_url")

    @staticmethod
    def getUsername():
        return config.get("admin login info", "username")

    @staticmethod
    def getPassword():
        return config.get("admin login info", "password")

    @staticmethod
    def getInvalidUsername():
        return config.get("admin login info", "invalid_username")
