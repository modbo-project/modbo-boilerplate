class Manager():
    __instance = None

    def __init__(self):
        pass

    @staticmethod
    def initialize():
        raise NotImplementedError

    @staticmethod
    def load():
        raise NotImplementedError