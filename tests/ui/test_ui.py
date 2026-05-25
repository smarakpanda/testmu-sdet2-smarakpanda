from logging import Logger

from pages import elements_page
from pages.elements_page import ElementsPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.decorators import logger
from utils.test_data_reader import get_login_data, get_web_table_form_addition_data


def get_username_and_password_for_qa():
    env = "qa"
    login_credentials = get_login_data(env)
    username = login_credentials["username"]
    password = login_credentials["password"]
    return username, password

def get_web_table_form_data(user_type):
    return get_web_table_form_addition_data(user_type)


class Tests:
    logger = Logger("Tests")

    def test_login_ui(self,page):
        # print(f" form data: {get_web_table_form_data("valid_user")}")
        home_page = HomePage(page)
        home_page_title = home_page.get_title()
        logger.info(f"Home Page Title: {home_page_title}")
        home_page.navigate_to_login_page()
        login_page_title = home_page.get_title()
        logger.info(f"Login Page Title: {login_page_title}")
        login_page = LoginPage(page)
        username,password = get_username_and_password_for_qa()
        login_page.login_to_book_store(username,password)
        login_page.is_logged_in_as(username)


    def test_add_web_table_data(self,page):
        web_table_form_details = get_web_table_form_data("valid_user")
        logger.info(f"Web Table Details: {web_table_form_details}")
        home_page = HomePage(page)
        home_page.navigate_to_elements_page()
        elements_page = ElementsPage(page)
        elements_page.navigate_to_add_web_tables_dialog()
        elements_page.enter_web_table_add_details(web_table_form_details)
        assert elements_page.validate_web_table_record_addition(web_table_form_details),"Web table addition failed."

