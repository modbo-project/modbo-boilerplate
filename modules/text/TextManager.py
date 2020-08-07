import yaml

from modules.pytg.Manager import Manager

from modules.pytg.ModulesLoader import ModulesLoader

class TextManager(Manager):
    @staticmethod
    def initialize():
        TextManager.__instance = TextManager()

        return

    @staticmethod
    def load():
        return TextManager.__instance

    def load_phrases(self, module="text", package="phrases", lang=None):
        module_folder = ModulesLoader.get_module_content_folder(module)

        if not lang:
            config_manager = ModulesLoader.load_manager("config")
            lang_settings = config_manager.load_settings_file("text", "lang")
            lang = lang_settings["default"]

        return yaml.safe_load(open("{}/text/{}/{}.yaml".format(module_folder, lang, package), "r", encoding="utf8"))
