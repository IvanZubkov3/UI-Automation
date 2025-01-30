import pytest
import yaml
import allure
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

# Load test data
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

@pytest.fixture
def driver():
    """Fixture to initialize WebDriver."""
    service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(config["base_url"])
    driver.maximize_window()
    time.sleep(3)
    login_page = LoginPage(driver)
    login_page.login(config["username"], config["password"])
    time.sleep(3)  # Ensure the page fully loads before proceeding
    yield driver
    driver.quit()

def test_add_to_cart(driver):
    """Test adding an item to the cart."""
    cart_page = CartPage(driver)
    cart_page.add_to_cart()
    time.sleep(3)  # Allow time for cart update
    cart_page.open_cart()
    assert cart_page.is_product_in_cart(config["product_name"]), "Product not found in the cart!"

def test_remove_from_cart(driver):
    """Test removing an item from the cart from the checkout window."""
    cart_page = CartPage(driver)
    cart_page.add_to_cart()  # Ensure an item is added before removing
    time.sleep(3)
    cart_page.open_cart()
    time.sleep(3)
    remove_button = driver.find_element(By.ID, "remove-sauce-labs-backpack")
    remove_button.click()
    time.sleep(3)
    assert not cart_page.is_product_in_cart(config["product_name"]), "Product was not removed from the cart!"

