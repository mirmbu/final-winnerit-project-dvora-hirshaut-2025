from api_requests.request_generator import RequestGenerator

class UserRequestGenerator(RequestGenerator):

    def __init__(self, base_url: str = "https://reqres.in/api"):
        super().__init__(base_url)


    def get_user(self, user_id: int):
        return self.get(f"/users/{user_id}")


    def get_resource_user(self, user_id: int):
        return self.get(f"/unknown/{user_id}")


    def create_user(self, data: dict):
        return self.post("/users", data)


    def update_user(self, user_id, data):
        return self.put(f"/users/{user_id}", data)