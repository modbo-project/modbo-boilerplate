class SuccessGuard():
    def __init__(self, expected_value = 1):
        self.__value = 0
        self.__expected_value = expected_value

    def verify(self):
        self.__value += 1

    def is_verified(self):
        return self.__value == self.__expected_value