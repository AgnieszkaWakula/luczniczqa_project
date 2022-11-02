import logging

import pytest

from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture(scope="class")
def session_driver():
    logging.getLogger('WDM').setLevel(logging.NOTSET)
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent= Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0")
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    browser.set_driver(webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options))
    browser.driver().maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def session_browser(session_driver):
    yield browser


