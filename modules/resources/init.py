import logging

from modules.pytg.ModulesLoader import ModulesLoader

from .ResourcesManager import ResourcesManager

def initialize():
    logging.info("Initializing resources module...")

    config_manager = ModulesLoader.load_manager("config")

    settings = config_manager.load_settings_file("resources")

    ResourcesManager.initialize()

def connect():
    pass

def load_manager():
    return ResourcesManager.load()

def depends_on():
    return ["config"]