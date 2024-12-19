import requests
from utils.config import BASE_URL, HEADERS


class API:
    """
        API class provides methods to perform CURD operations on REST APIs.
        It consists of POST, GET, PUT and DELETE requests.
    """
    @staticmethod
    def post(endpoint, data):
        """
        Perform a POST request
        :param endpoint: API endpoint
        :param data: JSON Request Payload
        :return: Response object
        """
        url = f'{BASE_URL}/{endpoint}'
        print("URL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", url)
        response = requests.post(url, headers=HEADERS, json=data)
        return response

    @staticmethod
    def get(endpoint):
        """
        Perform a GET request
        :param endpoint: API endpoint
        :return: Response object
        """
        url = f'{BASE_URL}/{endpoint}'
        print("URL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", url)
        response = requests.get(url, headers=HEADERS)
        return response

    @staticmethod
    def put(endpoint, id_param, data):
        """
        Perform a PUT request
        :param endpoint: API endpoint
        :param id_param: ID Query parameter
        :param data: JSON Request Payload
        :return: Response object
        """
        url = f'{BASE_URL}/{endpoint}/{id_param}'
        print("URL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", url)
        response = requests.put(url, headers=HEADERS, json=data)
        return response

    @staticmethod
    def delete(endpoint, id_param):
        """
        Perform a DELETE request
        :param endpoint: API endpoint
        :param id_param: ID Query parameter
        :return: Response object
        """
        url = f'{BASE_URL}/{endpoint}/{id_param}'
        print("URL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", url)
        response = requests.delete(url, headers=HEADERS)
        return response
