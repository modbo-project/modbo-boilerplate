import logging

from modules.pytg.load import manager

logger = logging.getLogger(__name__)

def welcome_message_handler(update, context):
    bot = context.bot

    message = update.message

    chat_id = message.chat.id

    new_chat_members = message.new_chat_members

    logger.info("Received welcome message update in chat {}".format(chat_id))

    phrases = manager("text").load_phrases("welcome_message")

    for new_member in new_chat_members:
        text = phrases["welcome_message"]

        text = text.replace("[first_name]", new_member.first_name)

        bot.sendMessage(
            chat_id = chat_id,
            text = text
        )