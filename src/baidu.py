from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import time


def create_driver(visible: bool = True) -> webdriver.Chrome:
    """Create and configure a Chrome WebDriver instance.
    
    Args:
        visible: Whether to run the browser in visible mode (default: True)
    
    Returns:
        Configured Chrome WebDriver instance
    """
    options = Options()
    if not visible:
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    
    service = Service(executable_path="./chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver


def open_baidu(driver: webdriver.Chrome, wait_seconds: int = 5) -> None:
    """Open Baidu website and wait for specified seconds.
    
    Args:
        driver: Chrome WebDriver instance
        wait_seconds: Time to wait after opening the page (default: 5)
    """
    driver.get("https://www.baidu.com/")
    time.sleep(wait_seconds)


def find_chat_textarea(driver: webdriver.Chrome, wait_seconds: int = 10) -> WebElement:
    """Find and return the chat textarea element.
    
    Args:
        driver: Chrome WebDriver instance
        wait_seconds: Maximum time to wait for the element (default: 10)
    
    Returns:
        Chat textarea WebElement
    
    Raises:
        TimeoutException: If element is not found within timeout
    """
    wait = WebDriverWait(driver, wait_seconds)
    return wait.until(EC.presence_of_element_located((By.ID, "chat-textarea")))


def find_search_button(driver: webdriver.Chrome, wait_seconds: int = 10) -> WebElement:
    """Find and return the search button element.
    
    Args:
        driver: Chrome WebDriver instance
        wait_seconds: Maximum time to wait for the element (default: 10)
    
    Returns:
        Search button WebElement
    
    Raises:
        TimeoutException: If element is not found within timeout
    """
    wait = WebDriverWait(driver, wait_seconds)
    return wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "svg_2cDwx.ai-search-btn-svg_vi_CZ")))


def search_poem(driver: webdriver.Chrome, poem_name: str) -> None:
    """Search for a poem on Baidu chat.
    
    Args:
        driver: Chrome WebDriver instance
        poem_name: Name of the poem to search
    """
    chat_textarea = find_chat_textarea(driver)
    chat_textarea.clear()
    chat_textarea.send_keys(poem_name)
    
    search_button = find_search_button(driver)
    search_button.click()
    
    # Wait for results to load
    time.sleep(5)


def verify_poem_content(driver: webdriver.Chrome, poem_lines: list[str]) -> bool:
    """Verify that all lines of a poem are present in the page source.
    
    Args:
        driver: Chrome WebDriver instance
        poem_lines: List of poem lines to verify
    
    Returns:
        True if all lines are found, False otherwise
    """
    page_source = driver.page_source
    all_lines_found = True
    
    for line in poem_lines:
        if line not in page_source:
            all_lines_found = False
            break
    
    return all_lines_found