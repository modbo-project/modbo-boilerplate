from .ModulesLoader import ModulesLoader

def manager(module_name):
    return ModulesLoader.load_manager(module_name)
