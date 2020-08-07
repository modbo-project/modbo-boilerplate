from modules.pytg.load import load_manager

def test():
    mockbot_manager = load_manager("mockbot")
    mockbot_manager.inject_updates([
        __load_test_update("simple_welcome")
    ])

    assert True

def __load_test_update(name):
    resources_manager = load_manager("resources")
    return resources_manager.load_resource("welcome_message_tests", name, path="test_updates", loader="json")