import logging, os

import queue

from modules.pytg.ModulesLoader import _InternalModulesLoader

from modules.pytg.development import dev_mode_on
from modules.pytg.initialization import initialize_module, connect_module, launch_main_module

logger = logging.getLogger(__name__)

def initialize_all_modules(ignored_modules=[]):
    # Initialize modules
    logger.info("Dynamically loading all modules...")

    # Loading dev modules (if needed)
    if dev_mode_on():
        logger.info("Dynamically loading development modules...")

        dev_modules = os.listdir("dev_modules") 
        for dev_module_name in dev_modules:
            if dev_module_name in ignored_modules:
                continue

            logger.info("Dynamically loading development module {}...".format(dev_module_name))

            initialize_module(dev_module_name, dev_module = True)

    modules = os.listdir("modules")
    modules.remove("pytg")

    for module_name in modules: 
        if module_name in ignored_modules:
            continue

        logger.info("Dynamically loading module {}...".format(module_name))

        initialize_module(module_name)

def connect_all_modules(ignored_modules=[]):
    # Connect modules
    logger.info("Connecting modules...")

    modules = os.listdir("modules")
    modules.remove("pytg")

    for module_name in modules: 
        if module_name in ignored_modules:
            continue

        logger.info("Dynamically connecting module {}...".format(module_name))

        connect_module(module_name)

def load_manager():
    # There shouldn't be any need for a manager in the pytg package
    return None

def depends_on():
    return []

def initialize(main_module="bot", dev_mode=False, modules_blocklist=[]):
    _InternalModulesLoader.initialize(dev_mode)

    initialize_all_modules(modules_blocklist)

def launch(main_module="bot", modules_blocklist=[]):
    connect_all_modules(modules_blocklist)

    launch_main_module(main_module)