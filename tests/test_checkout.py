import pytest
import yaml
import allure
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# Load test data
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

@pytest.fixture
def driver():
    """Fixture to initialize WebDriver."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(config["base_url"])
    login_page = LoginPage(driver)
    login_page.login(config["username"], config["password"])
    yield driver
    driver.quit()

def test_checkout_process(driver):
    """Test the full checkout process."""
    cart_page = CartPage(driver)
    cart_page.open_cart()
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_checkout_details("John", "Doe", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert "Thank you for your order!" in driver.page_source
