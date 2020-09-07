from .ModulesLoader import _InternalModulesLoader

def initialize_module(module_name, dev_module=False):
    _InternalModulesLoader.get_instance().initialize_module(module_name, dev_module)

def connect_module(module_name):
    _InternalModulesLoader.get_instance().connect_module(module_name)

def launch_main_module(module_name):
    _InternalModulesLoader.get_instance().launch_main_module(module_name)