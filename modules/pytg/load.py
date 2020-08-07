from .ModulesLoader import _InternalModulesLoader

def load_manager(module_name):
    return _InternalModulesLoader.get_instance().load_manager(module_name)

def get_module_content_folder(module_name):
    return _InternalModulesLoader.get_instance().get_module_content_folder(module_name)