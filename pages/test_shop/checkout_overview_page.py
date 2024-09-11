from ui_tests.pages.basepage import BasePage
from ui_tests.locators.locators import TestShopLocators


class CheckoutOverviewPage(BasePage):
    def finish_checkout_overview(self):
        self.click_button(locator=TestShopLocators.CHECKOUT_OVERVIEW_FINISH_BUTTON)
