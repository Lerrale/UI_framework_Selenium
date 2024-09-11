from ui_tests.pages.basepage import BasePage
from ui_tests.locators.locators import TestShopLocators


class ShopPage(BasePage):
    def add_to_cart_red_tshirt(self):
        self.click_button(
            locator=TestShopLocators.SHOPPING_PAGE_ADD_TO_CART_BUTTON_RED_TSHIRT
        )

    def go_to_cart(self):
        self.click_button(locator=TestShopLocators.SHOPPING_PAGE_SHOPPING_CART_BUTTON)
