from modules.pytg.load import load_manager

from telegram import Update

def test():
    mockbot_manager = load_manager("mockbot")
    bot = mockbot_manager.bot

    mockbot_manager.inject_update(__load_test_update("simple_welcome", bot))

    mockbot_manager.pull_updates()

    mockbot_manager.add_mock_response("POST", "sendMessage",
        {
            "{'chat_id': -436279640, 'text': 'Welcome to my group, Chat ID Echo!', 'disable_notification': False}": {}
        }
    )

    mockbot_manager.stop()

    assert False

def __load_test_update(name, bot):
    resources_manager = load_manager("resources")
    return Update.de_json(resources_manager.load_resource("welcome_message_tests", name, path="test_updates", loader="json"), bot)