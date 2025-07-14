from api_requests.request_generator import RequestGenerator


class UsersRequestGenerator(RequestGenerator):

    def __init__(self, base_url: str = "https://reqres.in/api"):
        super().__init__(base_url)


    def get_users(self, id: int):
        return self.get(f"/users?page={id}")


    def get_resource_users(self):
        return self.get("/unknown")


    def delayed_response(self, delay: int):
        return self.get(f"/users?delay={delay}")



