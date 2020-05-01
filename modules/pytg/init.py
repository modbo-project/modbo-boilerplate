import logging, os

import queue

from modules.pytg.ModulesLoader import ModulesLoader

def initialize():
    logging.info("Initializing pytg module...")

    # Initialize modules
    logging.info("Dynamically loading all modules...")

    modules = os.listdir("modules")
    modules.remove("pytg")

    for module_name in modules: 
        logging.info("Dynamically loading module {}...".format(module_name))

        ModulesLoader.initialize_module(module_name)

def connect():
    # Connect modules
    logging.info("Connecting modules...")

    modules = os.listdir("modules")
    modules.remove("pytg")

    for module_name in modules: 
        logging.info("Dynamically connecting module {}...".format(module_name))

        ModulesLoader.connect_module(module_name)

def load_manager():
    # There shouldn't be any need for a manager in the pytg package
    return None

def depends_on():
    return []