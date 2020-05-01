import logging, yaml, shutil, argparse

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    parser = argparse.ArgumentParser(description='PyTG command line remove module utility')
    parser.add_argument("--name")

    args = parser.parse_args()

    if not args.name:
        logging.error("No module specified")
        return

    logging.info("Removing module '{}'...".format(args.name))

    # Remove source
    logging.info("Removing source...")

    try:
        shutil.rmtree("modules/{}".format(args.name))
    except FileNotFoundError:
        logging.warning("Couldn't remove source files, folder not found")

    # Remove content
    logging.info("Removing content...")

    try:
        shutil.rmtree("content/{}".format(args.name))
    except FileNotFoundError:
        logging.warning("Couldn't remove content files, folder not found")


if __name__ == "__main__":
    main()