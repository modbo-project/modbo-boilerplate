import logging, yaml, shutil, argparse

from utils.scaffolding import get_folders_path

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    parser = argparse.ArgumentParser(description='PyTG command line remove module utility')
    parser.add_argument("--name")
    parser.add_argument("--dev", action="store_true")
    parser.add_argument("--source-only", action='store_true')

    args = parser.parse_args()

    if not args.name:
        logging.error("No module specified")
        return

    logging.info("Removing module '{}'...".format(args.name))

    # Remove source
    logging.info("Removing source...")

    modules_folder, content_folder = get_folders_path(args.dev)

    try:
        shutil.rmtree("{}/{}".format(modules_folder, args.name))
    except FileNotFoundError:
        logging.warning("Couldn't remove source files, folder not found")

    # Remove content
    if not args.source_only:
        logging.info("Removing content...")

        try:
            shutil.rmtree("{}/{}".format(content_folder, args.name))
        except FileNotFoundError:
            logging.warning("Couldn't remove content files, folder not found")


if __name__ == "__main__":
    main()