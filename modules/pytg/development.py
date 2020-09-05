from .ModulesLoader import _InternalModulesLoader

def add_reroute_rule(original_module, replacement_module):
    return _InternalModulesLoader.get_instance().add_reroute_rule(original_module, replacement_module)