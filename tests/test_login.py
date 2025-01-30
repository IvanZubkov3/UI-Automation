import pytest
import yaml
import allure
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# Load test data from config.yaml
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

@pytest.fixture
def driver():
    """Fixture to initialize WebDriver."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(config["base_url"])
    yield driver
    driver.quit()

def test_valid_login(driver):
    """Test valid login using credentials from config.yaml"""
    login_page = LoginPage(driver)
    login_page.login(config["username"], config["password"])
    assert "inventory.html" in driver.current_url

def test_invalid_login(driver):
    """Test login with invalid credentials."""
    login_page = LoginPage(driver)
    login_page.login(config["invalid_username"], config["invalid_password"])
    error_message = driver.find_element(By.XPATH, "//h3[contains(@data-test, 'error')]").text
    assert "Epic sadface" in error_message

def test_empty_login(driver):
    """Test login with empty fields."""
    login_page = LoginPage(driver)
    login_page.login("", "")
    error_message = driver.find_element(By.XPATH, "//h3[contains(@data-test, 'error')]").text
    assert "Username is required" in error_message
