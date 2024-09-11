import pytest
from pages.test_shop.shop_page import ShopPage
from pages.test_shop.cart_page import CartPage
from pages.test_shop.checkout_information_page import CheckoutInformationPage
from pages.test_shop.checkout_overview_page import CheckoutOverviewPage
from pages.test_shop.complete_page import CompletePage
import os


@pytest.mark.parametrize(
    "test_shop_login", [os.getenv("LOGIN_TESTSHOP_STANDART")], indirect=True
)
def test_login(browser, test_shop_login):

    shop_page = ShopPage(browser)
    shop_page.add_to_cart_red_tshirt()
    shop_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.go_checkout()

    checkout_information_page = CheckoutInformationPage(browser)
    checkout_information_page.fill_your_information()
    checkout_information_page.continue_from_checkout_information_page()

    checkout_overview_page = CheckoutOverviewPage(browser)
    checkout_overview_page.finish_checkout_overview()

    complete_page = CompletePage(browser)
    complete_page.check_text_in_elements()
