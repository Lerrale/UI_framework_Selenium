from ui_tests.pages.basepage import BasePage
from ui_tests.locators.locators import TestShopLocators


class CheckoutInformationPage(BasePage):
    def fill_your_information(self):
        self.fill_input_field(
            locator_field=TestShopLocators.CHECKOUT_INFORMATION_FIRSTNAME_INPUT,
            data="John",
        )
        self.fill_input_field(
            locator_field=TestShopLocators.CHECKOUT_INFORMATION_LASTNAME_INPUT,
            data="Malcovich",
        )
        self.fill_input_field(
            locator_field=TestShopLocators.CHECKOUT_INFORMATION_POSTALCODE_INPUT,
            data="1234",
        )

    def continue_from_checkout_information_page(self):
        self.click_button(locator=TestShopLocators.CHECKOUT_INFORMATION_CONTINUE_BUTTON)
