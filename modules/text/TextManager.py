import yaml

from modules.pytg.Manager import Manager

from modules.pytg.load import manager, get_module_content_folder

class TextManager(Manager):
    @staticmethod
    def initialize():
        TextManager.__instance = TextManager()

        return

    @staticmethod
    def load():
        return TextManager.__instance

    def load_phrases(self, module="text", package="phrases", lang=None):
        module_folder = get_module_content_folder(module)

        if not lang:
            lang_settings = manager("config").load_settings_file("text", "lang")
            lang = lang_settings["default"]

        return yaml.safe_load(open("{}/text/{}/{}.yaml".format(module_folder, lang, package), "r", encoding="utf8"))
