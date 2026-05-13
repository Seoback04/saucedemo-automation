import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:
    """
    Inventory/Products test cases for SauceDemo application.
    Tests cover product browsing, filtering, and sorting.
    """
    
    @pytest.fixture(autouse=True)
    def login_first(self, driver):
        """
        Login before each test.
        """
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        yield
    
    @pytest.mark.high
    @pytest.mark.inventory
    @pytest.mark.smoke
    def test_inventory_page_displays(self, driver):
        """
        Verify inventory page displays correctly after login.
        """
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_inventory_page_displayed(), "Inventory page should be displayed"
        assert inventory_page.get_product_count() > 0, "Products should be displayed"
    
    @pytest.mark.high
    @pytest.mark.inventory
    def test_product_list_contains_items(self, driver):
        """
        Verify products are displayed in the inventory.
        """
        inventory_page = InventoryPage(driver)
        
        product_count = inventory_page.get_product_count()
        assert product_count == 6, f"SauceDemo should have 6 products, got {product_count}"
        
        product_names = inventory_page.get_product_names()
        assert len(product_names) == 6, "Should display 6 product names"
        assert all(name for name in product_names), "All products should have names"
    
    @pytest.mark.high
    @pytest.mark.inventory
    def test_product_prices_displayed(self, driver):
        """
        Verify product prices are displayed.
        """
        inventory_page = InventoryPage(driver)
        
        prices = inventory_page.get_product_prices()
        assert len(prices) > 0, "Prices should be displayed"
        assert all(price for price in prices), "All products should have prices"
        assert all('$' in price for price in prices), "Prices should include currency symbol"
    
    @pytest.mark.medium
    @pytest.mark.inventory
    def test_sort_by_price_low_to_high(self, driver):
        """
        Test sorting products by price (low to high).
        """
        inventory_page = InventoryPage(driver)
        
        # Sort by price low to high
        inventory_page.sort_products("Price (low to high)")
        
        # Verify sort is applied
        prices = inventory_page.get_product_prices()
        converted_prices = [float(price.replace('$', '')) for price in prices]
        
        assert converted_prices == sorted(converted_prices), "Products should be sorted by price (low to high)"
    
    @pytest.mark.medium
    @pytest.mark.inventory
    def test_sort_by_price_high_to_low(self, driver):
        """
        Test sorting products by price (high to low).
        """
        inventory_page = InventoryPage(driver)
        
        # Sort by price high to low
        inventory_page.sort_products("Price (high to low)")
        
        # Verify sort is applied
        prices = inventory_page.get_product_prices()
        converted_prices = [float(price.replace('$', '')) for price in prices]
        
        assert converted_prices == sorted(converted_prices, reverse=True), \
            "Products should be sorted by price (high to low)"
    
    @pytest.mark.medium
    @pytest.mark.inventory
    def test_click_product(self, driver):
        """
        Test clicking on a product to view details.
        """
        inventory_page = InventoryPage(driver)
        
        # Get product name before clicking
        product_names = inventory_page.get_product_names()
        first_product = product_names[0]
        
        # Click first product
        inventory_page.click_product(0)
        
        # Verify page changed (URL should contain 'inventory/item')
        assert "inventory/item" in driver.current_url or "item" in driver.current_url, \
            "Should navigate to product details page"
    
    @pytest.mark.medium
    @pytest.mark.inventory
    def test_add_multiple_products_to_cart(self, driver):
        """
        Test adding multiple products to cart.
        """
        inventory_page = InventoryPage(driver)
        
        # Add 3 products to cart
        inventory_page.add_product_to_cart(0)
        inventory_page.add_product_to_cart(1)
        inventory_page.add_product_to_cart(2)
        
        # Verify cart count
        assert inventory_page.get_cart_item_count() == 3, "Cart should have 3 items"
    
    @pytest.mark.high
    @pytest.mark.inventory
    def test_logout_from_inventory(self, driver):
        """
        Test logout from inventory page.
        """
        inventory_page = InventoryPage(driver)
        
        inventory_page.logout()
        
        # Should be redirected to login page
        assert inventory_page.get_current_url() == "https://www.saucedemo.com/" or \
               "inventory" not in driver.current_url, "Should be logged out from inventory page"
    
    @pytest.mark.medium
    @pytest.mark.inventory
    def test_inventory_url_after_login(self, driver):
        """
        Verify correct URL after successful login.
        """
        inventory_page = InventoryPage(driver)
        
        current_url = inventory_page.get_current_url()
        assert "inventory" in current_url, "Should be on inventory URL after login"
    
    @pytest.mark.medium
    @pytest.mark.inventory
    def test_problem_user_login(self, driver):
        """
        Test with problem_user account (shows visual glitches but functions).
        """
        # First logout
        inventory_page = InventoryPage(driver)
        inventory_page.logout()
        
        # Login with problem_user
        login_page = LoginPage(driver)
        login_page.login("problem_user", "secret_sauce")
        
        # Should still be able to access inventory
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_inventory_page_displayed(), "Problem user should still access inventory"
        assert inventory_page.get_product_count() > 0, "Problem user should see products"


class TestProductDisplay:
    """
    Product display and formatting tests.
    """
    
    @pytest.fixture(autouse=True)
    def login_first(self, driver):
        """
        Login before each test.
        """
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        yield
    
    @pytest.mark.medium
    @pytest.mark.inventory
    def test_product_names_not_empty(self, driver):
        """
        Verify all product names are not empty.
        """
        inventory_page = InventoryPage(driver)
        
        product_names = inventory_page.get_product_names()
        
        for i, name in enumerate(product_names):
            assert name and len(name) > 0, f"Product {i} should have a non-empty name"
    
    @pytest.mark.medium
    @pytest.mark.inventory
    def test_product_prices_format(self, driver):
        """
        Verify product prices are in correct format.
        """
        inventory_page = InventoryPage(driver)
        
        prices = inventory_page.get_product_prices()
        
        for price in prices:
            assert price.startswith('$'), f"Price '{price}' should start with $"
            # Extract numeric part and verify it's a valid float
            price_numeric = price.replace('$', '').strip()
            try:
                float(price_numeric)
            except ValueError:
                pytest.fail(f"Price '{price}' should be a valid number")
    
    @pytest.mark.low
    @pytest.mark.inventory
    def test_sort_dropdown_exists(self, driver):
        """
        Verify sort dropdown is available.
        """
        inventory_page = InventoryPage(driver)
        
        # Try to access sort dropdown
        assert inventory_page.is_element_visible(inventory_page.SORT_DROPDOWN), \
            "Sort dropdown should be visible"
