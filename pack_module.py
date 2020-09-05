import logging, yaml, shutil, argparse

from git import Repo

from utils.scaffolding import get_folders_path

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    parser = argparse.ArgumentParser(description='PyTG command line pack module utility')
    parser.add_argument("--name")
    parser.add_argument("--dest")
    parser.add_argument("--dev", action="store_true")

    args = parser.parse_args()

    if not args.name:
        logging.error("No module specified")
        return

    if not args.dest:
        logging.error("No destination specified")
        return

    modules_folder, content_folder = get_folders_path(args.dev)

    source_folder = "{}/{}".format(modules_folder, args.name)
    content_folder = "{}/{}".format(content_folder, args.name)

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

    # Copy descriptor
    logging.info("Copying descriptor...")
    shutil.copyfile("{}/descriptor.yaml".format(source_folder), "{}/descriptor.yaml".format(destination_folder))

if __name__ == "__main__":
    main()