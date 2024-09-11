from selenium.webdriver.common.by import By


class TestShopLocators:
    # Login Page Locators
    LOGIN_PAGE_USERNAME_INPUT = (By.ID, "user-name")
    LOGIN_PAGE_PASSWORD_INPUT = (By.ID, "password")
    LOGIN_PAGE_LOGIN_BUTTON = (By.ID, "login-button")
    # Shopping Page Locators
    SHOPPING_PAGE_ADD_TO_CART_BUTTON_RED_TSHIRT = (
        By.ID,
        "add-to-cart-test.allthethings()-t-shirt-(red)",
    )
    SHOPPING_PAGE_SHOPPING_CART_BUTTON = (By.ID, "shopping_cart_container")
    # Cart Page Locators
    CART_PAGE_CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_PAGE_CHECKOUT_BUTTON = (By.ID, "checkout")
    # Checkout Information Page Locators
    CHECKOUT_INFORMATION_FIRSTNAME_INPUT = (By.ID, "first-name")
    CHECKOUT_INFORMATION_LASTNAME_INPUT = (By.ID, "last-name")
    CHECKOUT_INFORMATION_POSTALCODE_INPUT = (By.ID, "postal-code")
    CHECKOUT_INFORMATION_CONTINUE_BUTTON = (By.ID, "continue")
    # Checkout Overview Page Locators
    CHECKOUT_OVERVIEW_FINISH_BUTTON = (By.ID, "finish")
    # Complete Page Locators
    COMPLETE_PAGE_BACK_HOME_BUTTON = (By.ID, "back-to-products")
    COMPLETE_PAGE_BIG_TEXT = (By.CSS_SELECTOR, ".complete-header")
    COMPLETE_PAGE_LITTLE_TEXT = (By.CSS_SELECTOR, ".complete-text")
