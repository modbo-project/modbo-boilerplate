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
    print("setup")

def clear():
    print("clear")

def __load_test_update(name, bot):
    resources_manager = manager("resources")
    return Update.de_json(resources_manager.load_resource("welcome_message_tests", name, path="test_updates", loader="json"), bot)

# Tests

@mockbot_test(setup = setup, clear = clear)
def test():
    mockbot_manager = manager("mockbot")
    bot = mockbot_manager.bot

    mockbot_manager.inject_update(__load_test_update("simple_welcome", bot))

    mockbot_manager.pull_updates()

    mockbot_manager.add_mock_response("POST", "sendMessage",
        {
            "{'chat_id': -436279640, 'text': 'Welcome to my group, Chat ID Echo!', 'disable_notification': False}": {}
        }
    )

    mockbot_manager.stop()

    responses = mockbot_manager.pull_responses()

    for response in responses:
        print(response)

    assert True