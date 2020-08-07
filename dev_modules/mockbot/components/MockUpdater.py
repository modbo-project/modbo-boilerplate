import logging

from telegram.ext import Updater

class MockUpdater(Updater):
    def __init__(self, mock_bot):
        super(MockUpdater, self).__init__(bot = mock_bot, use_context = True)

        self.__updates = []

    def inject_update(self, update):
        self.__updates.append(update)

    def pull_updates(self):
        for update in self.__updates:
            self.update_queue.put(update)

        self.__updates.clear()

    def _start_polling(self, poll_interval, timeout, read_latency, bootstrap_retries, clean,
                       allowed_updates):  # pragma: no cover
        # Thread target of thread 'updater'. Runs in background, pulls
        # updates from Telegram and inserts them in the update queue of the
        # Dispatcher.

        self.logger.debug('Updater thread started (polling)')

        self._bootstrap(bootstrap_retries, clean=clean, webhook_url='', allowed_updates=None)

        self.logger.debug('Bootstrap done')

        return True