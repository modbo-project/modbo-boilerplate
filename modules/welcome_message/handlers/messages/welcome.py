import logging

from modules.pytg.ModulesLoader import ModulesLoader

logger = logging.getLogger(__name__)

def welcome_message_handler(update, context):
    bot = context.bot

    message = update.message

    chat_id = message.chat.id

    new_chat_members = message.new_chat_members

    print("Welcome")

    logger.info("Received welcome message update in chat {}".format(chat_id))

    text_manager = ModulesLoader.load_manager("text")
    phrases = text_manager.load_phrases("welcome_message")

    for new_member in new_chat_members:
        text = phrases["welcome_message"]

        text = text.replace("[first_name]", new_member.first_name)

        bot.sendMessage(
            chat_id = chat_id,
            text = text
        )