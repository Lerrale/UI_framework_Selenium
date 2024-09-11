from ui_tests.pages.basepage import BasePage
from ui_tests.locators.locators import TestShopLocators


class CartPage(BasePage):
    def go_checkout(self):
        self.click_button(locator=TestShopLocators.CART_PAGE_CHECKOUT_BUTTON)
