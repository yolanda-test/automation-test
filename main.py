# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Selenium example: open Chrome and navigate to Baidu with visible browser by default.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def open_baidu(visible: bool = True, wait_seconds: int = 5):
    """Launch Chrome and open https://www.baidu.com/.

    visible=True will start a normal (visible) browser window. Set visible=False to run headless.
    This function uses Selenium 4+ which includes selenium-manager to obtain the correct chromedriver automatically.
    """
    options = Options()
    if not visible:
        # Use the new headless mode flag for recent Chrome/Selenium
        options.add_argument("--headless=new")
    # Optional: make the browser start maximized
    options.add_argument("--start-maximized")
    # Create the Chrome WebDriver with the chromedriver in the current directory
    service = Service(executable_path="./chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.baidu.com/")
    # wait a bit so user can see the page before quitting
    time.sleep(wait_seconds)
    return driver





def test_baidu_chat(driver, wait_seconds: int = 10):
    """Test Baidu chat functionality:
    1. Verify input box id="chat-textarea" exists
    2. Input "沁园春雪" in the input box
    3. Click the button with class="svg_2cDwx ai-search-btn-svg_vi_CZ"
    4. Verify the page contains the full text of "沁园春雪"
    """
    try:
        # Wait for chat textarea to be present
        wait = WebDriverWait(driver, wait_seconds)
        chat_textarea = wait.until(EC.presence_of_element_located((By.ID, "chat-textarea")))
        print("✓ Chat textarea found")

        # Input "沁园春雪"
        chat_textarea.send_keys("沁园春雪")
        print("✓ Input text '沁园春雪' completed")

        # Wait for and click the search button
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "svg_2cDwx.ai-search-btn-svg_vi_CZ")))
        search_button.click()
        print("✓ Search button clicked")

        # Wait for the result to load
        time.sleep(10)  # Adjusted to allow more time for result loading

        # Verify the page contains the full poem text
        poem_lines = [
            "北国风光，千里冰封，万里雪飘。",
            "望长城内外，惟余莽莽；大河上下，顿失滔滔。",
            "山舞银蛇，原驰蜡象，欲与天公试比高。",
            "须晴日，看红装素裹，分外妖娆。",
            "江山如此多娇，引无数英雄竞折腰。",
            "惜秦皇汉武，略输文采；唐宗宋祖，稍逊风骚。",
            "一代天骄，成吉思汗，只识弯弓射大雕。",
            "俱往矣，数风流人物，还看今朝。"
        ]
        
        page_source = driver.page_source
        
        # Check each line of the poem
        all_lines_found = True
        for line in poem_lines:
            if line in page_source:
                print(f"✓ Found line: {line}")
            else:
                print(f"✗ Missing line: {line}")
                all_lines_found = False
        
        if all_lines_found:
            print("✓ All lines of the poem found on page")
            return True
        else:
            print("✗ Not all lines of the poem found on page")
            return False
    except Exception as e:
        print(f"✗ Error during test: {e}")
        import traceback
        traceback.print_exc()  # Print full traceback for debugging
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 打开可视化的 Chrome 并访问百度，等待 8 秒后退出。
    driver = open_baidu(visible=True, wait_seconds=8)
    # 测试百度聊天功能
    test_baidu_chat(driver)
    driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
