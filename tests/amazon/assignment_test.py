from logging import Logger

import pytest

from pages.amazon_pages.amazon_product_page import AmazonProductPage
from pages.amazon_pages.home_page import AmazonHomePage


class TestAmazon:
    logger = Logger("TestAmazon")

    @pytest.mark.parametrize(
        "product_name",
        [
            "Apple iPhone 16",
            "Samsung Galaxy S25"
        ]
    )

    def test_add_product_to_cart(self,page,product_name):
        home = AmazonHomePage(page)

        # home.navigate_to_home_page()
        home.search_product(product_name)
        price = home.open_first_available_result_and_return_price()
        home.assert_item_added_to_cart()

        # Amazon often opens product in same tab,
        # but wait for page load.
        # page.wait_for_load_state("networkidle")

        # product = AmazonProductPage(page)
        #
        # price = product.get_price()

        print("\n" + "=" * 50)
        print(f"{product_name} PRICE: {price}")
        print("=" * 50)

        # product.add_to_cart()
