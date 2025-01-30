from selenium.webdriver.common.by import By

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")

    def logout(self):
        """Logs out the user by clicking the logout button."""
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.logout_button).click()
