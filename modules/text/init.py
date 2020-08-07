import logging

from modules.text.TextManager import TextManager

def initialize():
    logging.info("Initializing text module...")

    TextManager.initialize()

def connect():
    pass

def load_manager():
    return TextManager.load()

def depends_on():
    return []