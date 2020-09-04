import logging

from modules.pytg.ModulesLoader import ModulesLoader
from modules.pytg.development import add_reroute_rule

from .MockConfigManager import MockConfigManager

def initialize():
    logging.info("Initializing mock_config module...")

    MockConfigManager.initialize()

def connect():
    pass

def load_manager():
    return MockConfigManager.load() 

def depends_on():
    return ["config"]