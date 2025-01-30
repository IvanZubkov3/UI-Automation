from selenium.webdriver.common.by import By
import time
import allure

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[contains(@data-test, 'error')]")

    def login(self, username, password):
        """Performs login action"""
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        time.sleep(2)  # Allow time for login process

    def get_error_message(self):
        """Returns the error message if login fails"""
        return self.driver.find_element(*self.error_message).text
