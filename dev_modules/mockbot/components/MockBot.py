import logging

from telegram import Bot

from .MockRequest import MockRequest

class MockBot(Bot):
    def __init__(self):
        request = MockRequest()
        # self.__add_validation_mock_responses(request)

        super(MockBot, self).__init__(token=None, base_url="mock.bot/", request = request)

    def _validate_token(self, token):
        return "mock:token" 