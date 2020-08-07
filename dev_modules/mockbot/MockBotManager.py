import telegram, yaml

from telegram.ext import Updater

from modules.pytg.Manager import Manager
from modules.pytg.ModulesLoader import ModulesLoader

from .components.MockBot import MockBot
from .components.MockUpdater import MockUpdater

class MockBotManager(Manager):
    @staticmethod
    def initialize():
        MockBotManager.__instance = MockBotManager()

    @staticmethod
    def load():
        return MockBotManager.__instance

    def __init__(self):
        self.bot = MockBot()
        self.updater = MockUpdater(mock_bot = self.bot)

    def add_mock_response(self, method, endpoint, response):
        self.bot.request.add_mock_response(method, endpoint, response)

    def inject_updates(self, updates=[]):
        self.bot.request.add_mock_response("POST", "getUpdates", {
            "{'timeout': 10, 'limit': 100}": updates
        })

    def pull_updates(self):
        self.updater.pull_updates()