class ResourcesLoader():
    def load_resource(self, module, resource_id, path=""):
        raise NotImplementedError

    def save_resource(self, module, resource_id, data, path=""):
        raise NotImplementedError