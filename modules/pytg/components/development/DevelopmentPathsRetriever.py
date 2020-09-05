import logging, os

class DevelopmentPathsRetriever():
    def __init__(self):
        self.__reroute_rules = {}
        self.__dev_modules = []

    def add_dev_module(self, module_name):
        if not self.__is_dev_module(module_name):
            self.__dev_modules.append(module_name)
    
    def __is_dev_module(self, module_name):
        return module_name in self.__dev_modules

    def add_reroute_rule(self, original_module, replacement_module):
        self.__reroute_rules[original_module] = replacement_module

    def get_routed_module_name(self, module_name):
        if module_name in self.__reroute_rules.keys():
            return self.__reroute_rules[module_name]

        return module_name

    def get_module_content_folder(self, module_name):
        routed_module_name = self.get_routed_module_name(module_name)

        logging.info("Getting {} ({}) content folder...".format(module_name, routed_module_name))

        return "{}/{}".format(self.__get_root_content_folder(routed_module_name), routed_module_name)

    def get_module_folder(self, module_name):
        routed_module_name = self.get_routed_module_name(module_name)

        logging.info("Getting {} ({}) folder...".format(module_name, routed_module_name))

        return "{}/{}".format(self.__get_root_module_folder(routed_module_name), routed_module_name)

    def get_module_package(self, module_name):
        routed_module_name = self.get_routed_module_name(module_name)

        logging.info("Getting {} ({}) package...".format(module_name, routed_module_name))

        return "{}.{}".format(self.__get_root_module_folder(routed_module_name), routed_module_name)

    def __get_root_content_folder(self, module_name):
        if self.__is_dev_module(module_name):
            return "dev_content"
        else:
            return "content"

    def __get_root_module_folder(self, module_name):
        if self.__is_dev_module(module_name):
            return "dev_modules"
        else:
            return "modules"


