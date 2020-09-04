from telegram import Update

from modules.pytg.load import manager

def setup():
    pass

def cleanup():
    pass

def load_test_update(name, bot):
    resources_manager = manager("resources")
    return Update.de_json(resources_manager.load_resource("welcome_message_tests", name, path="test_updates", loader="json"), bot)