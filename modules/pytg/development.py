from .ModulesLoader import _InternalModulesLoader

def dev_mode_on():
    return _InternalModulesLoader.get_instance().dev_mode_on()

def add_reroute_rule(original_module, replacement_module):
    return _InternalModulesLoader.get_instance().add_reroute_rule(original_module, replacement_module)

def register_mock_manager(module_name, mock_manager):
    return _InternalModulesLoader.get_instance().register_mock_manager(module_name, mock_manager)

def block_module(module_name):
    return _InternalModulesLoader.get_instance().block_module(module_name)