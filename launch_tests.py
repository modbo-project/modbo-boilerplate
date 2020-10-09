import logging, pytest, sys

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.WARN,
    )

    if len(sys.argv) == 1:
        args = ["dev_modules/", "--cov=modules", "-v"]
    else:
        args = sys.argv[1:]

    pytest.main(args)
