import logging, yaml, shutil, argparse

from git import Repo

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    parser = argparse.ArgumentParser(description='PyTG command line add module utility')
    parser.add_argument("--folder")
    parser.add_argument("--repo")
    parser.add_argument("--subfolder")
    parser.add_argument("--source-only", action="store_true")

    args = parser.parse_args()

    if not args.folder and not args.repo:
        logging.error("No source template specified")
        return

    logging.info("Recognizing template...")

    if args.folder:
        source_folder = args.folder
    elif args.repo:
        Repo.clone_from(args.repo, "repo_tmp/")
        if args.subfolder:
            source_folder = "repo_tmp/{}".format(args.subfolder)
        else:
            source_folder = "repo_tmp/"

    descriptor = yaml.safe_load(open("{}/descriptor.yaml".format(source_folder), "r"))

    logging.info("Adding module '{}' from template {}...".format(descriptor['module_name'], args.folder))

    src_destination_folder = "modules/{}".format(descriptor["module_name"])
    content_destination_folder = "content/{}".format(descriptor["module_name"])

    # Copy source
    logging.info("Copying source...")
    shutil.copytree("{}/src".format(source_folder), src_destination_folder)

    if not args.source_only and ("source_only" not in descriptor.keys() or not descriptor["source_only"]):
        logging.info("Copying content...")
        shutil.copytree("{}/dist_content".format(source_folder), content_destination_folder)

    # If repo is used, remove folder
    if args.repo:
        shutil.rmtree("repo_tmp/")

if __name__ == "__main__":
    main()