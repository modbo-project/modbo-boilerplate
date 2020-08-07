import logging

from modules.pytg.ModulesLoader import ModulesLoader

from telegram.ext import MessageHandler, Filters

from .handlers.messages.welcome import welcome_message_handler

def initialize():
    logging.info("Initializing welcome_message module...")

def connect():
    module_id = ModulesLoader.get_module_id("welcome_message")

    bot_manager = ModulesLoader.load_manager("bot")

    dispatcher = bot_manager.updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome_message_handler), group=module_id)

def load_manager():
    return None

def depends_on():
    return ["bot", "config", "text"]