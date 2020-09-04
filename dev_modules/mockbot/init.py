import logging

from modules.pytg.development import add_reroute_rule

from .MockBotManager import MockBotManager

def initialize():
    logging.info("Initializing mockbot module...")

    MockBotManager.initialize()

def connect():
    pass

def load_manager():
    return MockBotManager.load() 

def main():
    # Start polling
    logging.info("Mock bot polling.")

    manager = load_manager()

    manager.start()

def depends_on():
    return ["config"]