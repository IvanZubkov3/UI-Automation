from selenium.webdriver.common.by import By
import time

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.success_message = (By.CLASS_NAME, "complete-header")

    def enter_checkout_details(self, first_name, last_name, zip_code):
        """Fills in checkout details"""
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        time.sleep(2)

    def continue_checkout(self):
        """Clicks the continue button to proceed"""
        self.driver.find_element(*self.continue_button).click()
        time.sleep(2)

    def finish_checkout(self):
        """Completes the checkout process"""
        self.driver.find_element(*self.finish_button).click()
        time.sleep(2)

    def is_checkout_successful(self):
        """Checks if checkout was successful"""
        return "Thank you for your order!" in self.driver.find_element(*self.success_message).text
