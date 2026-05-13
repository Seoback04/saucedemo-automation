from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Login page object model.
    Contains all elements and methods related to the login page.
    """
    
    # Locators
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    PAGE_TITLE = (By.CLASS_NAME, "login_logo")
    
    # Page URL
    PAGE_URL = "https://www.saucedemo.com"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open_login_page(self):
        """Navigate to the login page."""
        self.get_url(self.PAGE_URL)
    
    def enter_username(self, username):
        """Enter username in the username field."""
        self.send_keys(self.USERNAME_FIELD, username)
    
    def enter_password(self, password):
        """Enter password in the password field."""
        self.send_keys(self.PASSWORD_FIELD, password)
    
    def click_login_button(self):
        """Click the login button."""
        self.click_element(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """
        Complete login process.
        
        Args:
            username (str): Username to login with
            password (str): Password to login with
        """
        self.open_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self):
        """Get the error message text."""
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except:
            return None
    
    def is_error_message_displayed(self):
        """Check if error message is displayed."""
        return self.is_element_visible(self.ERROR_MESSAGE)
    
    def is_login_page_displayed(self):
        """Check if login page is displayed."""
        return self.is_element_visible(self.PAGE_TITLE)
    
    def is_username_field_visible(self):
        """Check if username field is visible."""
        return self.is_element_visible(self.USERNAME_FIELD)
    
    def is_password_field_visible(self):
        """Check if password field is visible."""
        return self.is_element_visible(self.PASSWORD_FIELD)
    
    def is_login_button_visible(self):
        """Check if login button is visible."""
        return self.is_element_visible(self.LOGIN_BUTTON)
    
    def get_username_placeholder(self):
        """Get placeholder text from username field."""
        return self.get_attribute(self.USERNAME_FIELD, "placeholder")
    
    def get_password_placeholder(self):
        """Get placeholder text from password field."""
        return self.get_attribute(self.PASSWORD_FIELD, "placeholder")
    
    def clear_username_field(self):
        """Clear the username field."""
        self.find_element(self.USERNAME_FIELD).clear()
    
    def clear_password_field(self):
        """Clear the password field."""
        self.find_element(self.PASSWORD_FIELD).clear()
    
    def get_login_button_text(self):
        """Get the text of the login button."""
        return self.get_text(self.LOGIN_BUTTON)
