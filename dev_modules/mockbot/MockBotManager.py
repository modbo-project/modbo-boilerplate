import telegram, yaml, logging, time

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

        self.__logger = logging.getLogger(__name__)

    def add_mock_response(self, method, endpoint, response):
        self.bot.request.add_mock_response(method, endpoint, response)

    def add_trigger(self, method, endpoint, trigger):
        self.bot.request.add_trigger(method, endpoint, trigger)

    def inject_update(self, update):
        self.updater.inject_update(update)

    def pull_updates(self):
        self.updater.pull_updates()

    def pull_responses(self):
        return self.bot.request.pull_responses()

    def start(self):
        self.add_mock_response("GET", "getMe", {
            "id": 0,
            "is_bot": True,
            "first_name": "Mock Bot",
            "username": "MockBot",
            "can_join_groups": True,
            "can_read_all_group_messages": False,
            "supports_inline_queries": False
        })

        self.add_mock_response("GET", "getMyCommands", [])

        self.__logger.info("Starting MockBot...")

        self.updater.start_polling()

    def join(self):
        update_queue = self.updater.update_queue

        while update_queue.qsize() != 0:
            time.sleep(0.1)

    def stop(self):
        self.__logger.info("Stopping MockBot...")

        self.updater.stop()