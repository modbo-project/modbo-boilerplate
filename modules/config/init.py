import logging

from modules.config.ConfigManager import ConfigManager

def initialize():
    logging.info("Initializing config module...")

    ConfigManager.initialize()

def connect():
    pass

def load_manager():
    return ConfigManager.load()

def depends_on():
    return []