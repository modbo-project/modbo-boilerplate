import logging

from telegram.ext import Updater

class MockUpdater(Updater):
    def __init__(self, mock_bot):
        super(MockUpdater, self).__init__(bot = mock_bot)

    # def pull_updates(self):
    #     updates = self.bot.get_updates(self.last_update_id)

    #     if updates:
    #         if not self.running:
    #             self.logger.debug('Updates ignored and will be pulled again on restart')
    #         else:
    #             for update in updates:
    #                 self.update_queue.put(update)
    #             self.last_update_id = updates[-1].update_id + 1

    #     print(self.update_queue)

