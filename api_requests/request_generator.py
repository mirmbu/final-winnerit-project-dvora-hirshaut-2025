import requests
from requests import Response
from dotenv import load_dotenv
import os


load_dotenv()

class RequestGenerator:

    def __init__(self, base_url: str):
        self.__base_url = base_url
        self.__headers = {"x-api-key": os.getenv("X_API_KEY")}


    def get(self, endpoint: str):
        return requests.get(f"{self.__base_url}{endpoint}", headers=self.__headers, verify=False)


    def post(self, endpoint: str, data: dict):
        return requests.post(f"{self.__base_url}{endpoint}", headers=self.__headers, json=data, verify=False)


    def put(self, endpoint: str, data: dict):
        return requests.put(f"{self.__base_url}{endpoint}", headers=self.__headers, json=data, verify=False)


    def patch(self, endpoint: str, data: dict):
        return requests.patch(f"{self.__base_url}{endpoint}", headers=self.__headers, json=data, verify=False)


    def delete(self, endpoint: str):
        return requests.delete(f"{self.__base_url}{endpoint}", headers=self.__headers, verify=False)


    def validate_status_code(self, response: Response, expected_status_code: int):
        assert response.status_code == expected_status_code




