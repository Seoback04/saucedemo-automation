from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Inventory/Products page object model.
    Contains all elements and methods related to the products/inventory page.
    """
    
    # Locators
    INVENTORY_CONTAINER = (By.CLASS_NAME, "inventory_container")
    PRODUCT_ITEM = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_inventory_page_displayed(self):
        """Check if inventory page is displayed."""
        return self.is_element_visible(self.INVENTORY_CONTAINER)
    
    def get_product_count(self):
        """Get the number of products displayed."""
        products = self.find_elements(self.PRODUCT_ITEM)
        return len(products)
    
    def get_product_names(self):
        """Get all product names."""
        products = self.find_elements(self.PRODUCT_NAME)
        return [product.text for product in products]
    
    def get_product_prices(self):
        """Get all product prices."""
        prices = self.find_elements(self.PRODUCT_PRICE)
        return [price.text for price in prices]
    
    def add_product_to_cart(self, product_index=0):
        """
        Add a product to cart by index.
        
        Args:
            product_index (int): Index of the product to add (0-based)
        """
        buttons = self.find_elements(self.ADD_TO_CART_BUTTON)
        if product_index < len(buttons):
            buttons[product_index].click()
    
    def add_product_to_cart_by_name(self, product_name):
        """
        Add a specific product to cart by name.
        
        Args:
            product_name (str): Name of the product to add
        """
        locator = (By.XPATH, f"//div[contains(text(), '{product_name}')]/ancestor::div[@class='inventory_item']//button")
        self.click_element(locator)
    
    def click_cart_icon(self):
        """Click on the shopping cart icon."""
        self.click_element(self.CART_ICON)
    
    def get_cart_item_count(self):
        """Get the number of items in the cart."""
        try:
            return int(self.get_text(self.CART_BADGE))
        except:
            return 0
    
    def is_cart_badge_displayed(self):
        """Check if cart badge is displayed."""
        return self.is_element_visible(self.CART_BADGE)
    
    def sort_products(self, sort_option):
        """
        Sort products by option.
        
        Args:
            sort_option (str): Sort option (e.g., 'Price (low to high)', 'Price (high to low)', etc.)
        """
        self.click_element(self.SORT_DROPDOWN)
        option_locator = (By.XPATH, f"//option[contains(text(), '{sort_option}')]")
        self.click_element(option_locator)
    
    def click_product(self, product_index=0):
        """
        Click on a product to view details.
        
        Args:
            product_index (int): Index of the product to click
        """
        products = self.find_elements(self.PRODUCT_ITEM)
        if product_index < len(products):
            products[product_index].click()
    
    def open_menu(self):
        """Open the sidebar menu."""
        self.click_element(self.MENU_BUTTON)
    
    def logout(self):
        """Logout from the application."""
        self.open_menu()
        self.click_element(self.LOGOUT_BUTTON)
    
    def get_current_url(self):
        """Get the current page URL."""
        return self.driver.current_url
    
    def is_sorted_by(self, sort_type):
        """
        Check if products are sorted by a specific type.
        
        Args:
            sort_type (str): Type of sort ('price_low_to_high', 'price_high_to_low', 'name_asc', 'name_desc')
        
        Returns:
            bool: True if products are sorted correctly, False otherwise
        """
        prices = self.get_product_prices()
        
        if sort_type == 'price_low_to_high':
            converted_prices = [float(price.replace('$', '')) for price in prices]
            return converted_prices == sorted(converted_prices)
        elif sort_type == 'price_high_to_low':
            converted_prices = [float(price.replace('$', '')) for price in prices]
            return converted_prices == sorted(converted_prices, reverse=True)
        
        return False
