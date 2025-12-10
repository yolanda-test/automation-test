import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def setup_browser():
    """Setup and teardown browser instance for tests"""
    options = Options()
    # Use headless mode by default for CI/CD
    options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    
    # Create Chrome WebDriver with chromedriver in current directory
    service = Service(executable_path="./chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    
    # Navigate to Baidu
    driver.get("https://www.baidu.com/")
    
    # Yield driver for tests to use
    yield driver
    
    # Teardown: quit the driver
    driver.quit()


@pytest.fixture()
def wait_for_chat_element(setup_browser):
    """Wait for chat textarea to be present and return it"""
    driver = setup_browser
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.presence_of_element_located((By.ID, "chat-textarea")))


@pytest.mark.baidu
@pytest.mark.chat
def test_chat_textarea_exists(setup_browser):
    """Test that the chat textarea element exists on Baidu page"""
    driver = setup_browser
    wait = WebDriverWait(driver, 10)
    chat_textarea = wait.until(EC.presence_of_element_located((By.ID, "chat-textarea")))
    assert chat_textarea is not None
    assert chat_textarea.is_displayed()
    assert chat_textarea.is_enabled()


@pytest.mark.baidu
@pytest.mark.chat
@pytest.mark.parametrize("input_text, expected_lines", [
    (
        "沁园春雪",
        [
            "北国风光，千里冰封，万里雪飘。",
            "望长城内外，惟余莽莽；大河上下，顿失滔滔。",
            "山舞银蛇，原驰蜡象，欲与天公试比高。",
            "须晴日，看红装素裹，分外妖娆。",
            "江山如此多娇，引无数英雄竞折腰。",
            "惜秦皇汉武，略输文采；唐宗宋祖，稍逊风骚。",
            "一代天骄，成吉思汗，只识弯弓射大雕。",
            "俱往矣，数风流人物，还看今朝。"
        ]
    )
])
def test_chat_functionality(setup_browser, wait_for_chat_element, input_text, expected_lines):
    """Test Baidu chat functionality with different inputs"""
    driver = setup_browser
    chat_textarea = wait_for_chat_element
    
    # Clear any existing text and send the input
    chat_textarea.clear()
    chat_textarea.send_keys(input_text)
    
    # Wait for and click the search button
    wait = WebDriverWait(driver, 10)
    search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "svg_2cDwx.ai-search-btn-svg_vi_CZ")))
    search_button.click()
    
    # Wait for results to load
    time.sleep(5)  # Wait 5 seconds for results to load
    
    # Get page source and verify all expected lines are present
    page_source = driver.page_source
    all_lines_found = True
    for line in expected_lines:
        if line not in page_source:
            all_lines_found = False
    
    assert all_lines_found, "Not all lines of the poem found on page"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])