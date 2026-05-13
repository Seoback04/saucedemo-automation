from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """
    Cart page object model.
    Contains all elements and methods related to the shopping cart page.
    """
    
    # Locators
    CART_CONTAINER = (By.CLASS_NAME, "cart_list")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    EMPTY_CART_MESSAGE = (By.CLASS_NAME, "complete-text")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_cart_page_displayed(self):
        """Check if cart page is displayed."""
        return self.is_element_visible(self.CART_CONTAINER)
    
    def get_cart_items_count(self):
        """Get the number of items in the cart."""
        items = self.find_elements(self.CART_ITEM)
        return len(items)
    
    def get_item_names(self):
        """Get all item names in the cart."""
        items = self.find_elements(self.ITEM_NAME)
        return [item.text for item in items]
    
    def get_item_prices(self):
        """Get all item prices in the cart."""
        prices = self.find_elements(self.ITEM_PRICE)
        return [price.text for price in prices]
    
    def remove_item_from_cart(self, item_index=0):
        """
        Remove an item from cart by index.
        
        Args:
            item_index (int): Index of the item to remove (0-based)
        """
        remove_buttons = self.find_elements(self.REMOVE_BUTTON)
        if item_index < len(remove_buttons):
            remove_buttons[item_index].click()
    
    def click_continue_shopping(self):
        """Click continue shopping button."""
        self.click_element(self.CONTINUE_SHOPPING)
    
    def click_checkout(self):
        """Click checkout button."""
        self.click_element(self.CHECKOUT_BUTTON)
    
    def is_checkout_button_visible(self):
        """Check if checkout button is visible."""
        return self.is_element_visible(self.CHECKOUT_BUTTON)
