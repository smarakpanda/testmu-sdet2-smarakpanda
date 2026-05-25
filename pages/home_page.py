from pages.base_page import BasePage
from utils.decorators import log_decorator


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    BOOK_STORE_LINK =  "role=link[name='Book Store Application']"
    LOGIN_LINK = "role=link[name='Login']"
    ELEMENTS_LINK = "role=link[name='Elements']"

    @log_decorator
    def navigate_to_login_page(self):
        self.click(self.BOOK_STORE_LINK)
        self.click(self.LOGIN_LINK)

    @log_decorator
    def navigate_to_elements_page(self):
        self.click(self.ELEMENTS_LINK)
        self.click("role=link[name='Web Tables']")

