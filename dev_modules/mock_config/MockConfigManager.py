import yaml

from modules.pytg.Manager import Manager
from modules.pytg.load import get_module_content_folder

class MockConfigManager(Manager):
    @staticmethod
    def initialize():
        MockConfigManager.__instance = MockConfigManager()

    @staticmethod
    def load():
        return MockConfigManager.__instance

    def __init__(self):
        self.reset_config()

    def load_settings(self, module="config", file_name="settings"):
        return self.__config_map[module][file_name]

    def save_settings(self, settings, module="config", file_name="settings"):
        if module not in self.__config_map:
            self.__config_map[module] = {}

        self.__config_map[module][file_name] = settings

    add_mock_settings = save_settings

    def reset_config(self):
        self.__config_map = {}