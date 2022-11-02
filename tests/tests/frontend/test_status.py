import time

import pytest

from assertpy import assert_that

from tests.libs.pages.start_page import StartPage


@pytest.mark.frontend_1
@pytest.mark.usefixtures("session_browser")
class TestFrontend:

    def test_01_navigate_to_start_page(self, session_browser):
        session_browser.open_url("http://127.0.0.1:8080/start")
        assert_that(StartPage().return_page_header_text()).contains("EGNYTE API Tests")

    def test_02_verify_application_status_online(self):
        assert_that(StartPage().return_app_status_indicator_text()).is_equal_to("ONLINE")

    def test_03_click_on_set_offline_button(self):
        time.sleep(2)
        StartPage().click_set_offline_button()
        time.sleep(2)

    def test_05_verify_application_status_offline(self):
        assert_that(StartPage().return_app_status_indicator_text()).is_equal_to("OFFLINE")
