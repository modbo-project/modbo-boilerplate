class PathsRetriever():
    @staticmethod
    def get_module_content_folder(module_name):
        return "content/{}".format(module_name)

    @staticmethod
    def get_module_folder(module_name):
        return "modules/{}".format(module_name)

    @staticmethod
    def get_module_package(module_name):
        return "modules.{}".format(module_name)

