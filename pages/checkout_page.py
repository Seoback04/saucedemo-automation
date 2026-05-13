from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """
    Checkout page object model.
    Contains all elements and methods related to the checkout process.
    """
    
    # Step 1: Your Information
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    ZIP_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    
    # Step 2: Overview
    CHECKOUT_SUMMARY_CONTAINER = (By.CLASS_NAME, "summary_info")
    ORDER_SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    SHIPPING_LABEL = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    
    # Step 3: Completion
    CONFIRMATION_MESSAGE = (By.CLASS_NAME, "complete-text")
    DISPATCH_MESSAGE = (By.CLASS_NAME, "complete-header")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    # Step 1: Your Information
    def enter_first_name(self, first_name):
        """Enter first name."""
        self.send_keys(self.FIRST_NAME_FIELD, first_name)
    
    def enter_last_name(self, last_name):
        """Enter last name."""
        self.send_keys(self.LAST_NAME_FIELD, last_name)
    
    def enter_zip_code(self, zip_code):
        """Enter zip/postal code."""
        self.send_keys(self.ZIP_CODE_FIELD, zip_code)
    
    def fill_checkout_info(self, first_name, last_name, zip_code):
        """
        Fill all checkout information fields.
        
        Args:
            first_name (str): First name
            last_name (str): Last name
            zip_code (str): Zip/Postal code
        """
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)
    
    def click_continue(self):
        """Click continue button."""
        self.click_element(self.CONTINUE_BUTTON)
    
    def click_cancel(self):
        """Click cancel button."""
        self.click_element(self.CANCEL_BUTTON)
    
    def get_error_message(self):
        """Get error message text."""
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except:
            return None
    
    def is_error_displayed(self):
        """Check if error message is displayed."""
        return self.is_element_visible(self.ERROR_MESSAGE)
    
    # Step 2: Overview/Review
    def is_summary_page_displayed(self):
        """Check if checkout summary page is displayed."""
        return self.is_element_visible(self.CHECKOUT_SUMMARY_CONTAINER)
    
    def get_subtotal(self):
        """Get order subtotal."""
        return self.get_text(self.ORDER_SUBTOTAL)
    
    def get_total(self):
        """Get order total."""
        return self.get_text(self.TOTAL_LABEL)
    
    def click_finish(self):
        """Click finish button to complete order."""
        self.click_element(self.FINISH_BUTTON)
    
    # Step 3: Completion
    def is_order_confirmation_displayed(self):
        """Check if order confirmation page is displayed."""
        return self.is_element_visible(self.CONFIRMATION_MESSAGE)
    
    def get_confirmation_message(self):
        """Get the confirmation message text."""
        return self.get_text(self.CONFIRMATION_MESSAGE)
    
    def get_dispatch_message(self):
        """Get the dispatch/header message text."""
        return self.get_text(self.DISPATCH_MESSAGE)
    
    def complete_checkout(self, first_name, last_name, zip_code):
        """
        Complete the entire checkout process.
        
        Args:
            first_name (str): First name
            last_name (str): Last name
            zip_code (str): Zip/Postal code
        """
        self.fill_checkout_info(first_name, last_name, zip_code)
        self.click_continue()
        self.click_finish()
