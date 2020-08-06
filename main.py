import telegram, logging, threading, datetime, argparse, sys

from telegram.ext import Updater, MessageHandler, CommandHandler, Filters 

from modules.pytg.init import launch 

from utils.load import *

def __main():
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
    parser.add_argument("--devmode", action="store_true")

    args = parser.parse_args()

    main_module = args.main_module
    reroute_args = args.reroute
    dev_mode = args.devmode
    
    if not main_module:
        main_module = "bot"

    if reroute_args:
        reroute_rules = parse_reroute_rules(reroute_args)
    else:
        reroute_rules = None

    launch(main_module, dev_mode, reroute_rules)

if __name__ == '__main__':
    __main()
