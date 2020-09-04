import pytest

from modules.pytg.development import add_reroute_rule
from modules.pytg.load import manager

from modules.pytg.init import initialize, launch

from dev_modules.welcome_message_tests.integration.utils import setup_environment, teardown_environment, load_test_update

@pytest.fixture(autouse=True)
def test_container():
    setup_environment()
    yield
    teardown_environment()

# Tests
def test_simple_welcome():
    mockbot_manager = manager("mockbot")

    bot = mockbot_manager.bot

    mockbot_manager.inject_update(load_test_update("simple_welcome", bot))

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
    
    mockbot_manager.join()

    assert success