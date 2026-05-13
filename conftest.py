import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    """
    Fixture to initialize and provide WebDriver instance.
    Automatically takes screenshot on test failure.
    """
    # Initialize Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Uncomment for headless mode
    # options.add_argument("--headless")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    # Set implicit wait
    driver.implicitly_wait(10)
    
    yield driver
    
    # Teardown - Close browser
    driver.quit()


@pytest.fixture(scope="function")
def firefox_driver():
    """
    Fixture to initialize and provide Firefox WebDriver instance.
    """
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")
    # Uncomment for headless mode
    # options.add_argument("--headless")
    
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )
    
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()


@pytest.fixture(autouse=True)
def log_test_name(request):
    """
    Automatically log test name at the beginning and end of each test.
    """
    print(f"\n{'='*60}")
    print(f"Starting Test: {request.node.name}")
    print(f"{'='*60}")
    
    yield
    
    print(f"\n{'='*60}")
    print(f"Completed Test: {request.node.name}")
    print(f"{'='*60}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Make test results available to fixtures.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
