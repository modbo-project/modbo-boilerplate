import logging

from modules.pytg.ModulesLoader import ModulesLoader

from .MockBotManager import MockBotManager

def initialize():
    logging.info("Initializing mockbot module...")

    ModulesLoader.add_reroute_rule("bot", "mockbot")

    MockBotManager.initialize()

def connect():
    pass

def load_manager():
    return MockBotManager.load() 

def main():
    # Start polling
    logging.info("Mock bot polling.")

    manager = load_manager()

    manager.add_mock_response("GET", "getMe", {
        "id": 0,
        "is_bot": True,
        "first_name": "Mock Bot",
        "username": "MockBot",
        "can_join_groups": True,
        "can_read_all_group_messages": False,
        "supports_inline_queries": False
    })

    manager.add_mock_response("GET", "getMyCommands", [])

    manager.updater.start_polling()

def depends_on():
    return ["config"]