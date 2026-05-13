from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """
    Base page class with common Selenium operations.
    All page objects inherit from this class.
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
    def get_url(self, url):
        """Navigate to a specific URL."""
        self.driver.get(url)
    
    def find_element(self, locator):
        """Find a single element."""
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        """Find multiple elements."""
        return self.driver.find_elements(*locator)
    
    def click_element(self, locator):
        """Click on an element."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        """Send text to an input field."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text from an element."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text
    
    def is_element_visible(self, locator):
        """Check if an element is visible."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    def is_element_present(self, locator):
        """Check if an element is present in the DOM."""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False
    
    def wait_for_element(self, locator, timeout=10):
        """Wait for an element to be visible."""
        self.wait = WebDriverWait(self.driver, timeout)
        self.wait.until(EC.visibility_of_element_located(locator))
    
    def scroll_to_element(self, locator):
        """Scroll to an element."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def get_attribute(self, locator, attribute):
        """Get attribute value from an element."""
        element = self.find_element(locator)
        return element.get_attribute(attribute)
    
    def switch_to_frame(self, locator):
        """Switch to an iframe."""
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)
    
    def switch_to_default_content(self):
        """Switch back to default content."""
        self.driver.switch_to.default_content()
    
    def get_current_url(self):
        """Get current page URL."""
        return self.driver.current_url
    
    def get_page_title(self):
        """Get page title."""
        return self.driver.title
    
    def refresh_page(self):
        """Refresh the current page."""
        self.driver.refresh()
    
    def accept_alert(self):
        """Accept JavaScript alert."""
        self.driver.switch_to.alert.accept()
    
    def dismiss_alert(self):
        """Dismiss JavaScript alert."""
        self.driver.switch_to.alert.dismiss()
    
    def get_alert_text(self):
        """Get text from JavaScript alert."""
        return self.driver.switch_to.alert.text
    
    def move_to_element(self, locator):
        """Move mouse to an element."""
        element = self.find_element(locator)
        self.actions.move_to_element(element).perform()
    
    def double_click(self, locator):
        """Double click on an element."""
        element = self.find_element(locator)
        self.actions.double_click(element).perform()
    
    def right_click(self, locator):
        """Right click on an element."""
        element = self.find_element(locator)
        self.actions.context_click(element).perform()
    
    def drag_and_drop(self, source_locator, target_locator):
        """Drag an element and drop it on another element."""
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        self.actions.drag_and_drop(source, target).perform()
    
    def take_screenshot(self, filename):
        """Take a screenshot of the current page."""
        self.driver.save_screenshot(f"screenshots/{filename}.png")
    
    def execute_script(self, script, *args):
        """Execute JavaScript code."""
        return self.driver.execute_script(script, *args)
