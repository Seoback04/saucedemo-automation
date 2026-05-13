import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout:
    """
    Checkout test cases for SauceDemo application.
    Tests cover complete purchase flow from cart to order confirmation.
    """
    
    @pytest.fixture(autouse=True)
    def login_and_add_product(self, driver):
        """
        Fixture to login and add product to cart before each test.
        """
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_inventory_page_displayed(), "Should be on inventory page after login"
        
        # Add first product to cart
        inventory_page.add_product_to_cart(0)
        
        yield
    
    @pytest.mark.critical
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_complete_purchase_flow(self, driver):
        """
        TC-CHECKOUT-001: Complete purchase flow from cart to order confirmation.
        
        Test Steps:
        1. Login with valid credentials (done in fixture)
        2. Add product to cart
        3. Click shopping cart icon
        4. Click checkout button
        5. Enter customer information (First name, Last name, Zip code)
        6. Click Continue
        7. Review order details
        8. Click Finish
        9. Verify order confirmation page
        """
        inventory_page = InventoryPage(driver)
        
        # Navigate to cart
        inventory_page.click_cart_icon()
        
        cart_page = CartPage(driver)
        assert cart_page.is_cart_page_displayed(), "Should be on cart page"
        assert cart_page.get_cart_items_count() == 1, "Cart should have 1 item"
        
        # Proceed to checkout
        cart_page.click_checkout()
        
        checkout_page = CheckoutPage(driver)
        # Fill in customer information
        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.click_continue()
        
        # Verify summary page
        assert checkout_page.is_summary_page_displayed(), "Should be on checkout summary page"
        
        # Complete order
        checkout_page.click_finish()
        
        # Verify order confirmation
        assert checkout_page.is_order_confirmation_displayed(), "Should be on order confirmation page"
        assert "Thank you" in checkout_page.get_confirmation_message() or "Order" in checkout_page.get_dispatch_message(), \
            "Should show confirmation message"
    
    @pytest.mark.critical
    @pytest.mark.checkout
    def test_checkout_empty_first_name(self, driver):
        """
        Checkout with empty first name field.
        """
        inventory_page = InventoryPage(driver)
        inventory_page.click_cart_icon()
        
        cart_page = CartPage(driver)
        cart_page.click_checkout()
        
        checkout_page = CheckoutPage(driver)
        # Leave first name empty, enter other fields
        checkout_page.enter_last_name("Doe")
        checkout_page.enter_zip_code("12345")
        checkout_page.click_continue()
        
        # Should show error
        assert checkout_page.is_error_displayed(), "Error should be displayed for missing first name"
    
    @pytest.mark.critical
    @pytest.mark.checkout
    def test_checkout_empty_last_name(self, driver):
        """
        Checkout with empty last name field.
        """
        inventory_page = InventoryPage(driver)
        inventory_page.click_cart_icon()
        
        cart_page = CartPage(driver)
        cart_page.click_checkout()
        
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name("John")
        # Leave last name empty
        checkout_page.enter_zip_code("12345")
        checkout_page.click_continue()
        
        assert checkout_page.is_error_displayed(), "Error should be displayed for missing last name"
    
    @pytest.mark.critical
    @pytest.mark.checkout
    def test_checkout_empty_zip_code(self, driver):
        """
        Checkout with empty zip code field.
        """
        inventory_page = InventoryPage(driver)
        inventory_page.click_cart_icon()
        
        cart_page = CartPage(driver)
        cart_page.click_checkout()
        
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name("John")
        checkout_page.enter_last_name("Doe")
        # Leave zip code empty
        checkout_page.click_continue()
        
        assert checkout_page.is_error_displayed(), "Error should be displayed for missing zip code"
    
    @pytest.mark.high
    @pytest.mark.checkout
    def test_cancel_checkout(self, driver):
        """
        Test cancel button in checkout.
        """
        inventory_page = InventoryPage(driver)
        inventory_page.click_cart_icon()
        
        cart_page = CartPage(driver)
        cart_page.click_checkout()
        
        checkout_page = CheckoutPage(driver)
        checkout_page.click_cancel()
        
        # Should be back on cart page
        assert cart_page.is_cart_page_displayed() or "cart" in driver.current_url, "Should return to cart page"
    
    @pytest.mark.high
    @pytest.mark.checkout
    def test_multiple_items_checkout(self, driver):
        """
        Test checkout with multiple items in cart.
        """
        inventory_page = InventoryPage(driver)
        
        # Add second product
        inventory_page.add_product_to_cart(1)
        
        # Navigate to cart
        inventory_page.click_cart_icon()
        
        cart_page = CartPage(driver)
        assert cart_page.get_cart_items_count() == 2, "Cart should have 2 items"
        
        # Proceed with checkout
        cart_page.click_checkout()
        
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("Jane", "Smith", "54321")
        checkout_page.click_continue()
        
        # Verify order
        assert checkout_page.is_summary_page_displayed(), "Should be on checkout summary page"
        checkout_page.click_finish()
        
        assert checkout_page.is_order_confirmation_displayed(), "Should show order confirmation"


class TestCart:
    """
    Shopping cart test cases.
    """
    
    @pytest.mark.high
    @pytest.mark.checkout
    def test_add_product_to_cart(self, driver):
        """
        Test adding a product to cart.
        """
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_inventory_page_displayed(), "Should be on inventory page"
        
        # Add product to cart
        inventory_page.add_product_to_cart(0)
        
        # Verify cart badge
        assert inventory_page.get_cart_item_count() == 1, "Cart should show 1 item"
    
    @pytest.mark.high
    @pytest.mark.checkout
    def test_remove_product_from_cart(self, driver):
        """
        Test removing a product from cart.
        """
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(0)
        inventory_page.click_cart_icon()
        
        cart_page = CartPage(driver)
        assert cart_page.get_cart_items_count() == 1, "Cart should have 1 item"
        
        cart_page.remove_item_from_cart(0)
        assert cart_page.get_cart_items_count() == 0, "Cart should be empty after removal"
    
    @pytest.mark.medium
    @pytest.mark.checkout
    def test_continue_shopping(self, driver):
        """
        Test continue shopping button in cart.
        """
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(0)
        inventory_page.click_cart_icon()
        
        cart_page = CartPage(driver)
        cart_page.click_continue_shopping()
        
        # Should be back on inventory page
        assert inventory_page.is_inventory_page_displayed(), "Should return to inventory page"
    
    @pytest.mark.medium
    @pytest.mark.checkout
    def test_view_cart_items(self, driver):
        """
        Test viewing items in cart.
        """
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(0)
        inventory_page.add_product_to_cart(1)
        inventory_page.click_cart_icon()
        
        cart_page = CartPage(driver)
        assert cart_page.get_cart_items_count() == 2, "Cart should have 2 items"
        
        # Verify item names are displayed
        item_names = cart_page.get_item_names()
        assert len(item_names) == 2, "Should display 2 item names"
        assert all(name for name in item_names), "All items should have names"
