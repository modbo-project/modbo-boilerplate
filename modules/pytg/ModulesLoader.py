import importlib, logging

from .components.production.PathsRetriever import PathsRetriever
from .components.development.DevelopmentPathsRetriever import DevelopmentPathsRetriever

class _InternalModulesLoader():
    _instance = None

    @staticmethod
    def initialize(dev_mode = False):
        _InternalModulesLoader._instance = _InternalModulesLoader(dev_mode)

    def __init__(self, dev_mode):
        self.__loaded_modules = []
        self.__dev_mode = dev_mode

        self.logger = logging.getLogger("ModulesLoader")

        if self.__dev_mode:
            self.__paths_retriever = DevelopmentPathsRetriever()
        else:
            self.__paths_retriever = PathsRetriever()
    
    def dev_mode_on(self):
        return self.__dev_mode

    def add_reroute_rule(self, original_module, replacement_module):
        if not self.__dev_mode:
            self.logger.warning("Can't add reroute rule ({} := {}). Adding reroute rule while not in dev mode is not supported, skipping".format(original_module, replacement_module))
            return

        self.__paths_retriever.add_reroute_rule(original_module, replacement_module)

    def get_module_content_folder(self, module_name):
        return self.__paths_retriever.get_module_content_folder(module_name)

    def get_module_folder(self, module_name):
        return self.__paths_retriever.get_module_folder(module_name)

    def get_module_package(self, module_name):
        return self.__paths_retriever.get_module_package(module_name)

    def get_module_id(self, module_name):
        return self.__loaded_modules.index(module_name)

    def initialize_module(self, module_name, dev_module=False):
        if self.is_module_loaded(module_name):
            return

        if dev_module:
            self.__paths_retriever.add_dev_module(module_name)

        # Solve dependencies
        dependencies = self.get_module_dependencies(module_name)

        for dependency in dependencies:
            self.initialize_module(dependency)

        self.__get_module_initializer(module_name).initialize()

        self.__loaded_modules.append(module_name)

    def is_module_loaded(self, module_name):
        return module_name in self.__loaded_modules

    def connect_module(self, module_name):
        self.__get_module_initializer(module_name).connect()

    def load_manager(self, module_name):
        return self.__get_module_initializer(module_name).load_manager()

    def get_module_dependencies(self, module_name):
        return self.__get_module_initializer(module_name).depends_on() 

    def launch_main_module(self, module_name):
        self.__get_module_initializer(module_name).main()

    def __get_module_initializer(self, module_name):
        return importlib.import_module("{}.init".format(self.get_module_package(module_name)))

# Support to static access to ModulesLoader before deprecation
class __StaticModulesLoaderAccess(type):
    def __getattr__(cls, key):
        logging.warning("Static access to ModulesLoader attribute is deprecated and will be removed in a future release. Port your code as soon as possible")
        return getattr(_InternalModulesLoader._instance, key)

class ModulesLoader(metaclass=__StaticModulesLoaderAccess):
    pass
