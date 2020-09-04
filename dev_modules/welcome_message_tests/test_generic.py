from modules.pytg.development import add_reroute_rule

from modules.pytg.load import manager

from telegram import Update

# Helper functions

def mockbot_test(setup, clear):
    def inner(func):
        setup()
        func()
        clear()

    return inner

def setup():
    # add_reroute_rule("bot", "mockbot")
    print("setup")

def clear():
    print("clear")

def __load_test_update(name, bot):
    resources_manager = manager("resources")
    return Update.de_json(resources_manager.load_resource("welcome_message_tests", name, path="test_updates", loader="json"), bot)

# Tests
@mockbot_test(setup = setup, clear = clear)
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
            "{'chat_id': -436279640, 'text': 'Welcome to my group, Chat ID Echo!', 'disable_notification': False}": success_guard
        }
    )

    mockbot_manager.stop()

    assert success