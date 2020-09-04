import logging, telegram, json

from telegram.utils.request import Request

class MockRequest(Request):
    def __init__(self):
        self.__response_map = {
            "get": {},
            "post": {},
            # "retrieve": {},
            # "download": {}
        }

        self.__trigger_map = {
            "get": {},
            "post": {},
            # "retrieve": {},
            # "download": {}
        }

        self.__sent_responses = []

        self.__logger = logging.getLogger(__name__)

        self._con_pool_size = 1

    def add_mock_response(self, method, endpoint, response, domain="mock.bot/mock:token"):
        method = method.lower()

        if method not in self.__response_map.keys():
            self.__logger.warning("Unable to register mock response ({}, {}, {}), unknown method {}".format(method))
            return

        self.__response_map[method]["{}/{}".format(domain, endpoint)] = response

    def add_trigger(self, method, endpoint, trigger, domain="mock.bot/mock:token"):
        method = method.lower()

        if method not in self.__trigger_map.keys():
            self.__logger.warning("Unable to register mock response ({}, {}, {}), unknown method {}".format(method))
            return

        self.__trigger_map[method]["{}/{}".format(domain, endpoint)] = trigger

    def get(self, url, timeout=None):
        try:
            trigger = self.__recover_trigger("get", url)

            if trigger:
                trigger()

            try:
                response_data = self.__response_map["get"][url]
                self.__send_response("GET", response_data)

                return response_data
            except KeyError:
                if not trigger:
                    self.__logger.warning("Unknown GET mock reaction for url {}".format(url))

                return None

        except Exception as e:
            self.__logger.error("Unknown exception on GET request with url {} ({})".format(url, e))
            return None

    def post(self, url, data, timeout=None):
        serialized_data = str(data)

        trigger = self.__recover_trigger("post", url)

        if trigger:
            if serialized_data in trigger.keys():
                trigger[serialized_data]()

        try:
            # Retrieve possible data dictionary for the given URL 
            data_dict = self.__response_map["post"][url]
        except KeyError:
            if not trigger:
                self.__logger.warning("Unknown POST mock reaction for url {}".format(url))

            return None

        try:
            # Look for the right data (if present)
            for key in data_dict:
                if key == serialized_data:
                    response_data = data_dict[key]

                    self.__send_response("POST", response_data)

                    return response_data

            # If not, return null
            self.__logger.warning("Unknown POST mock response data {} with url {} ".format(data, url))
            return None
        except Exception as e:
            self.__logger.error("Unknown exception on GET request with url {} and data {} ({})".format(url, data, e))
            return None

    def __recover_trigger(self, method, url):
        try:
            return self.__trigger_map[method][url]
        except KeyError:
            return None

    def pull_responses(self):
        current_responses = list(self.__sent_responses)

        self.__sent_responses.clear()

        return current_responses

    def __send_response(self, method, data):
        self.__sent_responses.append({
            "method": method,
            "data": data
        })

        return data