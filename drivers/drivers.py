import allure
from selenium import webdriver

def get_driver():
    """Initialize and return a WebDriver instance."""
    driver = webdriver.Chrome()  # Adjust if using Firefox/Edge
    driver.maximize_window()
    return driver

@allure.step("Navigating to {url}")
def navigate_to(driver, url):
    """Navigate to a URL and log details in Allure."""
    driver.get(url)
    allure.attach(driver.current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)
    allure.attach(driver.page_source, name="Page Source", attachment_type=allure.attachment_type.HTML)
