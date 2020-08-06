import logging, pytest

from modules.pytg.init import launch

DEBUG = True

if __name__ == '__main__':
    if DEBUG:
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO,
        )
    else:
        logging.basicConfig(level=logging.CRITICAL)

    launch(dev_mode = True)

    pytest.main()