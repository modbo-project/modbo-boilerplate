import pytest

from modules.pytg.development import add_reroute_rule

from modules.pytg.load import manager

from telegram import Update

def setup():
    pass

def cleanup():
    pass

@pytest.fixture(autouse=True)
def test_container():
    setup()
    yield
    cleanup()

def __load_test_update(name, bot):
    resources_manager = manager("resources")
    return Update.de_json(resources_manager.load_resource("welcome_message_tests", name, path="test_updates", loader="json"), bot)

# Tests
def test_simple_welcome():
    mockbot_manager = manager("mockbot")
    bot = mockbot_manager.bot

    mockbot_manager.inject_update(__load_test_update("simple_welcome", bot))

    mockbot_manager.pull_updates()

    success = False

    def success_guard():
        nonlocal success
        success = True

    mockbot_manager.add_trigger("POST", "sendMessage",
        {
            str({'chat_id': -436279640, 'text': 'Welcome to my group, Chat ID Echo!', 'disable_notification': False}): success_guard
        }
    )

    mockbot_manager.stop()

    assert success