from logging import Logger

from config.config import get_value_from_config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.decorators import logger
from utils.test_data_reader import get_user_data_api


def get_user_creds():
    env = get_value_from_config("environment")
    user_creds = get_user_data_api(env)
    username = user_creds["username"]
    password = user_creds["password"]
    return username, password


class TestE2E:
    logger = Logger("TestE2E")

    def test_e2e(self, account_client,page):
        username, password = get_user_creds()
        response = account_client.create_user(username, password)
        assert response.status == 201, f"User creation failed: {response.status}"

        home_page = HomePage(page)
        home_page.navigate_to_login_page()
        login_page_title = home_page.get_title()
        logger.info(f"Login Page Title: {login_page_title}")
        login_page = LoginPage(page)
        login_page.login_to_book_store(username,password)
        assert login_page.is_logged_in_as(username), "Login failed"




