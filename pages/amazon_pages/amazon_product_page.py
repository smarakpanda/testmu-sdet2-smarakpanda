from playwright.sync_api import Page

from pages.base_page import BasePage


class AmazonProductPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def get_price(self) -> str:
        whole = self.page.locator(".a-price-whole").first.text_content()
        fraction = self.page.locator(".a-price-fraction").first.text_content()

        return f"${whole}.{fraction}"

    def add_to_cart(self):
        self.page.locator("#add-to-cart-button").click()