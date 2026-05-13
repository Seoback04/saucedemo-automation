# Contributing to SauceDemo Automation Tests

Thank you for contributing to this automation testing project! Please follow these guidelines to ensure smooth collaboration.

## Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/Seoback04/saucedemo-automation.git
cd saucedemo-automation
```

2. **Create a feature branch**
```bash
git checkout -b feature/your-feature-name
```

3. **Set up development environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Writing Tests

### Test Structure
- Place test files in the `tests/` directory
- Follow naming convention: `test_*.py`
- Use meaningful class and function names
- Include docstrings explaining what the test does

### Test Template
```python
import pytest
from pages.login_page import LoginPage

class TestLoginFeature:
    """Test cases for login feature."""
    
    @pytest.mark.critical
    @pytest.mark.login
    def test_valid_login(self, driver):
        """
        Test description here.
        
        Test Steps:
        1. Step one
        2. Step two
        3. Expected result
        """
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        assert "inventory" in driver.current_url
```

### Markers
Use pytest markers to categorize tests:
- `@pytest.mark.critical` - Critical functionality
- `@pytest.mark.high` - High priority
- `@pytest.mark.medium` - Medium priority
- `@pytest.mark.low` - Low priority
- `@pytest.mark.login` - Login related
- `@pytest.mark.checkout` - Checkout related
- `@pytest.mark.inventory` - Inventory related
- `@pytest.mark.smoke` - Smoke tests

### Page Objects
Create page object classes in the `pages/` directory for each page:
```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class YourPage(BasePage):
    """Page object for your page."""
    
    # Define locators
    ELEMENT_LOCATOR = (By.ID, "element_id")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def your_method(self):
        """Method description."""
        self.click_element(self.ELEMENT_LOCATOR)
```

## Running Tests Locally

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_login.py -v

# Run specific test
pytest tests/test_login.py::TestLogin::test_valid_login -v

# Run with HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html

# Run with specific marker
pytest tests/ -v -m critical
```

## Code Style

- Follow PEP 8 style guide
- Use descriptive variable and function names
- Add docstrings to all functions
- Keep functions small and focused
- Use explicit waits instead of sleeps

## Commit Messages

Write clear commit messages following this format:

```
Brief description (50 chars or less)

More detailed explanation if needed (wrap at 72 chars)
- Point 1
- Point 2

```

Examples:
```
Add login validation tests

- Test valid credentials
- Test invalid password
- Test locked user account
```

## Pull Requests

1. **Before submitting:**
   - Run all tests locally: `pytest tests/ -v`
   - Check code style compliance
   - Update README if needed
   - Add descriptive PR title and description

2. **PR Title Format:**
   ```
   [FEATURE/BUG/TEST] Brief description
   ```

3. **PR Description Should Include:**
   - What changes were made
   - Why these changes were needed
   - How to test the changes
   - Any related issues

## Reporting Issues

If you find a bug or want to suggest an improvement:

1. Check if issue already exists
2. Create detailed issue with:
   - Clear title
   - Description of the problem
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)

## Test Best Practices

✅ **DO:**
- Use explicit waits
- Keep tests independent
- Use meaningful assertions
- Follow the Arrange-Act-Assert pattern
- Use Page Object Model
- Test one thing per test
- Use test data that's easy to understand

❌ **DON'T:**
- Use sleep() instead of explicit waits
- Create dependencies between tests
- Mix multiple concerns in one test
- Use hardcoded values (except test data)
- Skip or ignore failing tests
- Test implementation details
- Use generic assertion messages

## Test Data

Test credentials for SauceDemo:
- **standard_user** / **secret_sauce** (normal user)
- **locked_out_user** / **secret_sauce** (locked account)
- **problem_user** / **secret_sauce** (visual glitches)

URL: https://www.saucedemo.com

## Continuous Integration

GitHub Actions automatically runs tests on:
- Every push to main branch
- Every pull request
- Daily at 2:00 AM UTC

All tests must pass before merging to main.

## Questions or Need Help?

- Create an issue for questions
- Review existing documentation
- Check similar test files for examples

---

**Thank you for contributing!**


---

**Last Updated:** May 2026
**Status:** ✅ Active

Thank you for your interest in contributing to this project!
