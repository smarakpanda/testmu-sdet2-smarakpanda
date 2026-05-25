from config.config import get_value_from_config
from utils.test_data_reader import get_user_data_api


class TestAPI:

    def test_create_user(self,account_client):
        env = get_value_from_config("environment")
        user_creds = get_user_data_api(env)
        username = user_creds["username"]
        password = user_creds["password"]

        response = account_client.create_user(username,password)
        print(response.status)
        print(response.text())
        assert response.status == 201
