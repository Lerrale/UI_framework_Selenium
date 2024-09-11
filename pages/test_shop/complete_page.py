from ui_tests.pages.basepage import BasePage
from ui_tests.locators.locators import TestShopLocators


class CompletePage(BasePage):
    def check_text_in_elements(self):
        self.check_text_in_element(
            text_in_element="Thank you for your order!",
            locator=TestShopLocators.COMPLETE_PAGE_BIG_TEXT,
        )
        self.check_text_in_element(
            text_in_element="Your order has been dispatched, and will arrive just as fast as the pony can get there!",
            locator=TestShopLocators.COMPLETE_PAGE_LITTLE_TEXT,
        )
