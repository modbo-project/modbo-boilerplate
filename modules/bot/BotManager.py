import telegram, yaml

from telegram.ext import Updater

from modules.pytg.Manager import Manager
from modules.pytg.ModulesLoader import ModulesLoader

class BotManager(Manager):
    @staticmethod
    def initialize():
        BotManager.__instance = BotManager()

    @staticmethod
    def load():
        return BotManager.__instance

    def __init__(self):
        config_manager = ModulesLoader.load_manager("config")

        settings = config_manager.load_settings_file("bot", "token")

        self.bot = telegram.Bot(settings["token"])
        self.updater = Updater(settings["token"], use_context=True)

        return