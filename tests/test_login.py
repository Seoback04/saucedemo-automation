import pytest
from pages.login_page import LoginPage


class TestLogin:
    """
    Login test cases for SauceDemo application.
    Tests cover valid login, invalid credentials, and error scenarios.
    """
    
    @pytest.mark.critical
    @pytest.mark.login
    @pytest.mark.smoke
    def test_valid_login(self, driver):
        """
        TC-LOGIN-001: Valid user login with standard account.
        
        Test Steps:
        1. Navigate to SauceDemo login page
        2. Enter valid username (standard_user)
        3. Enter valid password (secret_sauce)
        4. Click login button
        5. Verify successful login and redirect to inventory page
        """
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        # Verify successful login by checking URL change
        assert "inventory" in driver.current_url, "User should be redirected to inventory page"
        
        # Additional verification could check for user name display
        assert login_page.get_current_url() != login_page.PAGE_URL, "Login page should not be displayed"
    
    @pytest.mark.critical
    @pytest.mark.login
    def test_login_invalid_password(self, driver):
        """
        TC-LOGIN-002: Login with invalid password.
        
        Test Steps:
        1. Navigate to login page
        2. Enter valid username (standard_user)
        3. Enter invalid password (wrong_password)
        4. Click login button
        5. Verify error message is displayed
        """
        login_page = LoginPage(driver)
        login_page.login("standard_user", "wrong_password")
        
        # Verify error message is displayed
        assert login_page.is_error_message_displayed(), "Error message should be displayed"
        assert "do not match" in login_page.get_error_message().lower(), "Error message should indicate credential mismatch"
    
    @pytest.mark.critical
    @pytest.mark.login
    def test_login_locked_user(self, driver):
        """
        TC-LOGIN-003: Login attempt with locked user account.
        
        Test Steps:
        1. Navigate to login page
        2. Enter locked user username (locked_out_user)
        3. Enter correct password (secret_sauce)
        4. Click login button
        5. Verify error message about locked account
        """
        login_page = LoginPage(driver)
        login_page.login("locked_out_user", "secret_sauce")
        
        # Verify locked user error message
        assert login_page.is_error_message_displayed(), "Error message should be displayed for locked user"
        assert "locked" in login_page.get_error_message().lower(), "Error message should indicate user is locked"
    
    @pytest.mark.medium
    @pytest.mark.login
    def test_login_empty_username(self, driver):
        """
        TC-LOGIN-004: Login attempt with empty username field.
        
        Test Steps:
        1. Navigate to login page
        2. Leave username field empty
        3. Enter password (secret_sauce)
        4. Click login button
        5. Verify error message about required username
        """
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()
        
        # Verify error message
        assert login_page.is_error_message_displayed(), "Error message should be displayed"
        assert "required" in login_page.get_error_message().lower(), "Error should indicate username is required"
    
    @pytest.mark.medium
    @pytest.mark.login
    def test_login_empty_password(self, driver):
        """
        TC-LOGIN-005: Login attempt with empty password field.
        
        Test Steps:
        1. Navigate to login page
        2. Enter username (standard_user)
        3. Leave password field empty
        4. Click login button
        5. Verify error message about required password
        """
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.enter_username("standard_user")
        login_page.click_login_button()
        
        # Verify error message
        assert login_page.is_error_message_displayed(), "Error message should be displayed"
        assert "required" in login_page.get_error_message().lower(), "Error should indicate password is required"
    
    @pytest.mark.medium
    @pytest.mark.login
    def test_login_page_elements_visible(self, driver):
        """
        Verify all login page elements are visible and properly displayed.
        """
        login_page = LoginPage(driver)
        login_page.open_login_page()
        
        assert login_page.is_login_page_displayed(), "Login page should be displayed"
        assert login_page.is_username_field_visible(), "Username field should be visible"
        assert login_page.is_password_field_visible(), "Password field should be visible"
        assert login_page.is_login_button_visible(), "Login button should be visible"
    
    @pytest.mark.high
    @pytest.mark.login
    def test_login_invalid_username(self, driver):
        """
        Login attempt with invalid username.
        """
        login_page = LoginPage(driver)
        login_page.login("invalid_user", "secret_sauce")
        
        # Verify error message
        assert login_page.is_error_message_displayed(), "Error message should be displayed"
        assert "do not match" in login_page.get_error_message().lower(), "Error should indicate credential mismatch"
    
    @pytest.mark.high
    @pytest.mark.login
    def test_login_both_fields_empty(self, driver):
        """
        Login attempt with both username and password fields empty.
        """
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_login_button()
        
        # Verify error message
        assert login_page.is_error_message_displayed(), "Error message should be displayed"
