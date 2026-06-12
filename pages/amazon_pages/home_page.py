from logging import Logger

from playwright.sync_api import Page

from config import config
from pages.base_page import BasePage
from utils.decorators import log_decorator, logger


class AmazonHomePage(BasePage):
    logger = Logger("Amazon Home Page")

    def __init__(self, page: Page):
        super().__init__(page)

    def navigate_to_home_page(self):
        amazon_url = config.get_value_from_config("AMAZON_URL")
        self.navigate(amazon_url)

    @log_decorator
    def search_product(self, product_name: str):
        search_box = self.page.locator("#twotabsearchtextbox")
        search_box.fill(product_name)
        search_box.press("Enter")

    @log_decorator
    def open_first_available_result_and_return_price(self):
        logger.info("Finding first product with Add to cart")
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(2000)
        product = self._get_first_product_with_add_to_cart()
        if not product:
            raise Exception("No product with Add to cart found")
        price = self._extract_price(product)
        self._click_add_to_cart(product)
        return price

    def _get_first_product_with_add_to_cart(self):
        products = self.page.locator("[data-component-type='s-search-result']")
        count = products.count()
        for i in range(count):
            product = products.nth(i)
            if self._has_add_to_cart(product):
                logger.info(f"Valid product found at index {i}")
                return product
        return None

    def _has_add_to_cart(self, product):
        add_to_cart = product.get_by_role("button", name="Add to cart")
        return add_to_cart.count() > 0

    def _extract_price(self, product):
        try:
            price_whole = product.locator(".a-price-whole").first.inner_text().strip()
            price_fraction = product.locator(".a-price-fraction").first.inner_text().strip()
            price = f"{price_whole}{price_fraction}"

            logger.info(f"Extracted price: {price}")
            return price
        except Exception as e:
            logger.warning(f"Price extraction failed: {str(e)}")
            return None

    def _click_add_to_cart(self, product):
        add_to_cart = product.get_by_role("button", name="Add to cart")
        add_to_cart.first.wait_for(state="visible", timeout=10000)
        add_to_cart.first.scroll_into_view_if_needed()

        logger.info("Clicking Add to cart")
        add_to_cart.first.click(timeout=10000)

    @log_decorator
    def assert_item_added_to_cart(self):
        logger.info("Verifying item added to cart")

        cart_count = self.page.locator("#nav-cart-count")
        cart_count.wait_for(state="visible", timeout=10000)

        # Wait until cart count becomes > 0
        self.page.wait_for_function(
            """() => {
                const el = document.querySelector('#nav-cart-count');
                if (!el) return false;
                const value = parseInt(el.innerText.trim() || '0');
                return value > 0;
            }""",
            timeout=15000
        )

        final_text = cart_count.inner_text().strip()

        try:
            final_count = int(final_text)
        except:
            final_count = 0

        logger.info(f"Final cart count: {final_count}")

        assert final_count > 0, "Item was not added to cart"