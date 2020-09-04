import telegram, yaml

from telegram.ext import Updater

from modules.pytg.Manager import Manager

from modules.pytg.load import manager

class BotManager(Manager):
    @staticmethod
    def initialize():
        BotManager.__instance = BotManager()

    @staticmethod
    def load():
        return BotManager.__instance

    def connect(self):
        settings = manager("config").load_settings("bot", "token")

        self.bot = telegram.Bot(settings["token"])
        self.updater = Updater(settings["token"], use_context=True)

    def start_polling(self):
        self.updater.start_polling()