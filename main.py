# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Selenium example: open Chrome and navigate to Baidu with visible browser by default.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
    # Create the Chrome WebDriver (selenium-manager will download/use the right driver for Selenium 4+)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.baidu.com/")
    # wait a bit so user can see the page before quitting
    time.sleep(wait_seconds)
    return driver


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 打开可视化的 Chrome 并访问百度，等待 8 秒后退出。
    driver = open_baidu(visible=True, wait_seconds=8)
    driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
