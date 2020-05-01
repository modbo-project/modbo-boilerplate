import logging, yaml, shutil, argparse

from git import Repo

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    parser = argparse.ArgumentParser(description='PyTG command line pack module utility')
    parser.add_argument("--name")
    parser.add_argument("--dest")

    args = parser.parse_args()

    if not args.name:
        logging.error("No module specified")
        return

    if not args.dest:
        logging.error("No destination specified")
        return

    source_folder = "modules/{}".format(args.name)
    content_folder = "content/{}".format(args.name)

    destination_folder = args.dest

    logging.info("Packing module '{}' in folder {}...".format(args.name, args.dest))

    # Copy source
    logging.info("Copying source...")
    shutil.copytree(source_folder, "{}/src".format(destination_folder))

    # Copy content
    logging.info("Copying content...")

    try:
        shutil.copytree(content_folder, "{}/dist_content".format(destination_folder))
    except FileNotFoundError:
        logging.warning("Couldn't copy content files, folder not found")

if __name__ == "__main__":
    main()