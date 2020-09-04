import pytest, threading, logging

from telegram import Update

from modules.pytg.load import manager
from modules.pytg.init import initialize, launch
from modules.pytg.development import add_reroute_rule

def setup_environment():
    initialize(dev_mode = True)

    add_reroute_rule("bot", "mockbot")
    add_reroute_rule("config", "mock_config")

    manager("mock_config").add_mock_settings({
        "loaders": ["yaml", "json"],
        "default_loader": "yaml"
    }, "resources")

    manager("mock_config").add_mock_settings({
        "default": "en"
    }, "text", "lang")

    launch(main_module="mockbot")
    
def teardown_environment():
    manager("mockbot").stop()

def load_test_update(name, bot):
    resources_manager = manager("resources")
    return Update.de_json(resources_manager.load_resource("welcome_message_tests", name, path="test_updates", loader="json"), bot)