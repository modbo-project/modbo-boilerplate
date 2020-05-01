import telegram, logging, threading, datetime, argparse

from telegram.ext import Updater, MessageHandler, CommandHandler, Filters 

from modules.pytg.ModulesLoader import ModulesLoader

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

    args = parser.parse_args()

    main_module = args.main_module

    if not main_module:
        logging.error("No main module specified")
        return

    # Initialize PyTG module (initializes all modules)
    ModulesLoader.initialize_module("pytg")

    # Connect PyTG module (connects all modules)
    ModulesLoader.connect_module("pytg")

    # Launch main module
    ModulesLoader.launch_main_module(main_module)

if __name__ == '__main__':
    main()
