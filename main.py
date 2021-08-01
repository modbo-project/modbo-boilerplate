import logging, os

from modbo.init import boot, initialize, launch

def __main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    boot(False)
    initialize()
    launch(os.environ["MAIN_MODULE"])

if __name__ == '__main__':
    __main()
