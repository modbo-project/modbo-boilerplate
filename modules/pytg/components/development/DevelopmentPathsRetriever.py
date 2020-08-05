import logging

class DevelopmentPathsRetriever():
    def __init__(self, reroute_rules):
        self.reroute_rules = reroute_rules

    def get_routed_module_name(self, module_name):
        if module_name in self.reroute_rules.keys():
            return self.reroute_rules[module_name]

        return module_name

    def get_module_content_folder(self, module_name):
        routed_module_name = self.get_routed_module_name(module_name)

        logging.info("Getting {} ({}) content folder...".format(module_name, routed_module_name))

        return "content/{}".format(routed_module_name)

    def get_module_folder(self, module_name):
        routed_module_name = self.get_routed_module_name(module_name)

        logging.info("Getting {} ({}) folder...".format(module_name, routed_module_name))

        return "modules/{}".format(routed_module_name)

    def get_module_package(self, module_name):
        routed_module_name = self.get_routed_module_name(module_name)

        logging.info("Getting {} ({}) package...".format(module_name, routed_module_name))

        return "modules.{}".format(routed_module_name)

