from selene import be
from selene.support.jquery_style_selectors import s

from tests.libs.locators.start_page_locators import StartPageLocators


class StartPage(StartPageLocators):

    def return_page_header_text(self):
        s(self.START_PAGE_HEADER).should(be.visible)
        return s(self.START_PAGE_HEADER).text

    def return_app_status_indicator_text(self):
        s(self.START_PAGE_APP_STATUS_INDICATOR).should(be.visible)
        return s(self.START_PAGE_APP_STATUS_INDICATOR).text

    def click_set_online_button(self):
        s(self.START_PAGE_SET_ONLINE_BUTTON).click()

    def click_set_offline_button(self):
        s(self.START_PAGE_SET_OFFLINE_BUTTON).click()

    def return_students_table_last_row_text(self):
        s(self.START_PAGE_STUDENT_TABLE_LAST_ROW).should(be.visible)
        return s(self.START_PAGE_STUDENT_TABLE_LAST_ROW).text

    def return_universities_table_last_row_text(self):
        s(self.START_PAGE_UNIVERSITY_TABLE_LAST_ROW).should(be.visible)
        return s(self.START_PAGE_UNIVERSITY_TABLE_LAST_ROW).text
