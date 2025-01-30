from selenium.webdriver.common.by import By
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.ID, "shopping_cart_container")
        self.checkout_button = (By.ID, "checkout")
        self.remove_button = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        self.product_name = (By.CLASS_NAME, "inventory_item_name")
        self.add_to_cart_button = (By.XPATH, "//button[contains(text(), 'Add to cart')]")

    def open_cart(self):
        """Opens the cart page"""
        self.driver.find_element(*self.cart_icon).click()
        time.sleep(2)

    def add_to_cart(self):
        """Adds an item to the cart"""
        add_buttons = self.driver.find_elements(*self.add_to_cart_button)
        if add_buttons:
            add_buttons[0].click()  # Click the first available "Add to cart" button
            time.sleep(2)
        else:
            raise Exception("No 'Add to cart' button found!")

    def remove_item(self):
        """Adds an item first, then removes it from the cart"""
        self.add_to_cart()
        time.sleep(2)
        self.open_cart()
        time.sleep(2)
        try:
            remove_button = self.driver.find_element(*self.remove_button)
            remove_button.click()
            time.sleep(2)
        except:
            raise Exception("No 'Remove' button found!")

    def proceed_to_checkout(self):
        """Proceeds to checkout page"""
        self.driver.find_element(*self.checkout_button).click()
        time.sleep(2)

    def is_product_in_cart(self, product_name):
        """Checks if a product is in the cart"""
        cart_items = self.driver.find_elements(*self.product_name)
        return any(product.text == product_name for product in cart_items)

