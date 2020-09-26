import telegram, logging, threading, datetime, argparse, sys

from telegram.ext import Updater, MessageHandler, CommandHandler, Filters 

from modules.pytg.init import boot, initialize, launch 

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
    parser.add_argument("--devmode", action="store_true")

    args = parser.parse_args()

    main_module = args.main_module
    dev_mode = args.devmode
    
    if not main_module:
        main_module = "bot"

    boot(dev_mode)
    initialize()
    launch(main_module)

if __name__ == '__main__':
    __main()
