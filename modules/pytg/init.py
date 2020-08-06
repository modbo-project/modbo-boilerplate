import logging, os

import queue

from modules.pytg.ModulesLoader import ModulesLoader, _InternalModulesLoader

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

def launch(main_module="bot", dev_mode=False, reroute_rules=None):
    _InternalModulesLoader.initialize(dev_mode)

    # Add reroute rules (if any)
    if reroute_rules:
        for (original_module, replacement_module) in reroute_rules.items():
            ModulesLoader.add_reroute_rule(original_module, replacement_module)

    # Initialize PyTG module (initializes all modules)
    ModulesLoader.initialize_module("pytg")

    # Connect PyTG module (connects all modules)
    ModulesLoader.connect_module("pytg")

    # Launch main module
    ModulesLoader.launch_main_module(main_module)

