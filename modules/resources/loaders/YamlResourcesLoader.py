import yaml, logging

from modules.pytg.load import get_module_content_folder

from .ResourcesLoader import ResourcesLoader

class YamlResourcesLoader(ResourcesLoader):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def load_resource(self, module, resource_id, path):
        module_folder = get_module_content_folder(module)

        try:
            return yaml.safe_load(open("{}/{}/{}.yaml".format(module_folder, path, resource_id), "r"))
        except FileNotFoundError:
            self.logger.warning("Trying to access missing YAML resource '{}/{}' in module {}".format(path, resource_id, module))

            return None

    def save_resource(self, module, resource_id, data, path):
        module_folder = get_module_content_folder(module)

        yaml.safe_dump(data, open("{}/{}/{}.yaml".format(module_folder, path, resource_id), "w"))