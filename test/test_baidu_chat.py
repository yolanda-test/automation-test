import pytest
from typing import Generator
from selenium import webdriver
from src.baidu import create_driver, open_baidu, search_poem, verify_poem_content


@pytest.fixture(scope="module")
def browser() -> Generator[webdriver.Chrome, None, None]:
    """Fixture to create and manage a Chrome browser instance for tests.
    
    Scope: module - one browser instance per test module
    """
    driver = create_driver(visible=True)  # Run in headless mode for tests
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def baidu_page(browser: webdriver.Chrome) -> Generator[webdriver.Chrome, None, None]:
    """Fixture to open Baidu page before tests and provide the browser instance.
    
    Scope: module - Baidu page is opened once per test module
    """
    open_baidu(browser, wait_seconds=2)
    yield browser


@pytest.fixture
def qinyuanchunxue_poem() -> list[str]:
    """Fixture to provide the full text of the poem "Qinyuanchun·Snow" as a list of lines.
    """
    return [
        "北国风光，千里冰封，万里雪飘。",
        "望长城内外，惟余莽莽；大河上下，顿失滔滔。",
        "山舞银蛇，原驰蜡象，欲与天公试比高。",
        "须晴日，看红装素裹，分外妖娆。",
        "江山如此多娇，引无数英雄竞折腰。",
        "惜秦皇汉武，略输文采；唐宗宋祖，稍逊风骚。",
        "一代天骄，成吉思汗，只识弯弓射大雕。",
        "俱往矣，数风流人物，还看今朝。"
    ]


@pytest.mark.baidu
@pytest.mark.chat
def test_baidu_chat_functionality(baidu_page: webdriver.Chrome, qinyuanchunxue_poem: list[str]) -> None:
    """Test Baidu chat functionality for searching and displaying the poem "Qinyuanchun·Snow".
    
    Steps:
    1. Search for the poem "Qinyuanchun·Snow" in Baidu chat
    2. Verify that all lines of the poem are displayed in the search results
    """
    search_poem(baidu_page, "沁园春雪")
    assert verify_poem_content(baidu_page, qinyuanchunxue_poem), "Not all lines of the poem found on page"