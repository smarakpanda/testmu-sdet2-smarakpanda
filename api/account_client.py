class AccountClient:
    def __init__(self, api_client):
        self.api = api_client

    def create_user(self, username, password):
        payload = {
            "userName": username,
            "password": password
        }

        return self.api.post("/Account/v1/User", data=payload)