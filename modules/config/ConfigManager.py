import yaml

from modules.pytg.Manager import Manager
from modules.pytg.ModulesLoader import ModulesLoader

class ConfigManager(Manager):
    @staticmethod
    def initialize():
        ConfigManager.__instance = ConfigManager()

        return

    @staticmethod
    def load():
        return ConfigManager.__instance

    def load_settings_file(self, module="config", file_name="settings"):
        module_folder = ModulesLoader.get_module_content_folder(module)

        return yaml.safe_load(open("{}/config/{}.yaml".format(module_folder, file_name)))

    def save_settings_file(self, settings, module="config", file_name="settings"):
        module_folder = ModulesLoader.get_module_content_folder(module)

        yaml.safe_dump(settings, open("{}/config/{}.yaml".format(module_folder, file_name), "w"))