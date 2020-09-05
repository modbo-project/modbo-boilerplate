import pytest

from modules.pytg.development import add_reroute_rule
from modules.pytg.load import manager

from modules.pytg.testing.utils.triggers.success import SuccessGuard

from modules.pytg.init import initialize, launch

from dev_modules.welcome_message_tests.integration.utils import setup_environment, teardown_environment, load_test_update

@pytest.fixture(autouse=True)
def test_container():
    setup_environment()
    yield
    teardown_environment()

def test_simple_welcome():
    mockbot_manager = manager("mockbot")

    bot = mockbot_manager.bot

    mockbot_manager.inject_update(load_test_update("simple_welcome", bot))

    mockbot_manager.pull_updates()

    guard = SuccessGuard()

    mockbot_manager.add_trigger("POST", "sendMessage",
        {
            str({'chat_id': -436279640, 'text': 'Welcome to my group, Chat ID Echo!', 'disable_notification': False}): guard.verify
        }
    )
    
    mockbot_manager.join()

    assert guard.is_verified()

def test_multiple_welcome():
    mockbot_manager = manager("mockbot")

    bot = mockbot_manager.bot
    mockbot_manager.inject_update(load_test_update("multiple_welcome", bot))
    mockbot_manager.pull_updates()

    guard = SuccessGuard(3)

    mockbot_manager.add_trigger("POST", "sendMessage",
        {
            str({'chat_id': -436279640, 'text': 'Welcome to my group, User 0!', 'disable_notification': False}): guard.verify,
            str({'chat_id': -436279640, 'text': 'Welcome to my group, User 1!', 'disable_notification': False}): guard.verify,
            str({'chat_id': -436279640, 'text': 'Welcome to my group, User 2!', 'disable_notification': False}): guard.verify,
        }
    )
    
    mockbot_manager.join()

    assert guard.is_verified()