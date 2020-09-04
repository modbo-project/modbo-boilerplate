import logging

from modules.pytg.load import manager, get_module_id

from telegram.ext import MessageHandler, Filters

from .handlers.messages.welcome import welcome_message_handler

def initialize():
    logging.info("Initializing welcome_message module...")

def connect():
    module_id = get_module_id("welcome_message")

    dispatcher = manager("bot").updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome_message_handler), group=module_id)

def load_manager():
    return None

def depends_on():
    return ["bot", "config", "text"]