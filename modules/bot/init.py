import logging

from modules.bot.BotManager import BotManager

def initialize():
    logging.info("Initializing bot module...")

    BotManager.initialize()

def connect():
    pass

def load_manager():
    return BotManager.load() 

def main():
    # Start polling
    load_manager().start_polling()

    logging.info("Polling.")

def depends_on():
    return ["config"]