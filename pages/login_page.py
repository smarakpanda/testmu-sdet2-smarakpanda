from logging import Logger

from pages.base_page import BasePage
from utils.decorators import logger, log_decorator
from utils.test_data_reader import get_login_data


class LoginPage(BasePage):
    logger = Logger("LoginPage")

    def __init__(self,page):
        super().__init__(page)

    USERNAME_FIELD = "role=textbox[name='UserName']"
    PASSWORD_FIELD = "role=textbox[name='Password']"
    LOGIN_BUTTON = "role=button[name='Login']"
    USERNAME_LABEL = "#userName-value"

    def login_to_qa_environment(self):
        env = "qa"
        login_credentials = get_login_data(env)
        username = login_credentials["username"]
        password = login_credentials["password"]

        self.page.fill(self.USERNAME_FIELD,username)
        self.page.fill(self.PASSWORD_FIELD,password)
        self.page.click(self.LOGIN_BUTTON)


    @log_decorator
    def login_to_book_store(self,username,password):

        self.fill(self.USERNAME_FIELD,username)
        self.fill(self.PASSWORD_FIELD,password)
        self.click(self.LOGIN_BUTTON)

    @log_decorator
    def get_logged_in_user(self):
        username = self.get_text(self.USERNAME_LABEL)
        if not username:
            raise Exception(f"Locator {self.USERNAME_LABEL} not found.")
        return username


    @log_decorator
    def is_logged_in_as(self,username):
        logger.info(f"Checking if logged in as: {username}")
        return username == self.get_logged_in_user()




