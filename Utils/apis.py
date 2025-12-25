import requests
#import
class API:
    # Base URL for all API requests
    Base_URL = "http://jsonplaceholder.typicode.com/"

    def __init__(self):
        # Default headers for all requests
        self.headers = {
            "Content-Type": "application/json",
        }

    def get(self, endpoint):
        url = f"{API.Base_URL}{endpoint}"
        self.headers = {
            "Content-Type": "application/json",
        }
        response = requests.get(url, headers=self.headers)
        return response

    def post(self, endpoint, data):
        url = f"{API.Base_URL}{endpoint}"
        self.headers = {"Content-Type": "application/json"}

        response = requests.post(url, headers=self.headers, json=data)
        return response

    def put(self, endpoint, data):
        url = f"{API.Base_URL}{endpoint}"
        self.headers = {
            "Content-Type": "application/json",
        }
        response = requests.put(url, headers=self.headers, json=data)
        return response

    def delete(self, endpoint):
        url = f"{API.Base_URL}{endpoint}"
        self.headers = {
            "Content-Type": "application/json",
        }
        response = requests.delete(url, headers=self.headers)
        return response










