import telegram, logging, threading, datetime, argparse, sys

from telegram.ext import Updater, MessageHandler, CommandHandler, Filters 

from modules.pytg.ModulesLoader import ModulesLoader

from utils.load import *

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        # filename="pytg-bot.log"
    )

    logging.info(" ### Launching Bot... ### ")
    logging.info(str(datetime.datetime.now()))

    parser = argparse.ArgumentParser(description='PyTG command line launcher')
    parser.add_argument("--main-module")
    parser.add_argument("--reroute", action="append")

    args = parser.parse_args()

    main_module = args.main_module
    reroute_args = args.reroute

    dev_mode = False

    if not main_module:
        logging.error("No main module specified")

        sys.exit(1)

    # Formalize re-routes
    if reroute_args:
        dev_mode = True

        reroute_rules = parse_reroute_rules(reroute_args)

    # Inject development components in test mode
    if dev_mode:
        ModulesLoader.inject_dev_components_in_modules_loader(reroute_rules)
    else:
        ModulesLoader.inject_prod_components_in_modules_loader()

    # Initialize PyTG module (initializes all modules)
    ModulesLoader.initialize_module("pytg")

    # Connect PyTG module (connects all modules)
    ModulesLoader.connect_module("pytg")

    # Launch main module
    ModulesLoader.launch_main_module(main_module)

if __name__ == '__main__':
    main()
