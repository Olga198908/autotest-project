import pytest
import allure
from playwright.sync_api import sync_playwright, Page, expect
from data.data_page import *
from locators.locators_page import *

@pytest.fixture
def auth_login(page: Page):
    def auth_login_fync():
        with allure.step("Логин в систему"):
            page.goto(AUTH_URL, timeout=60000)
            page.fill(USERNAME_INPUT, VALID_USERNAME)
            page.fill(PASSWORD_INPUT, VALID_PASSWORD)
            page.click(LOGIN_BUTTON)
            expect(page.locator(DASHBOARD_HEADER)).to_be_visible()
            page.click(DASHBOARD_HEADER)
            page.click(PROFILE_DROPDOWN)
            page.click(LOGOUT_LINK)
            expect(page.locator(USERNAME_INPUT)).to_be_visible()

    return auth_login_fync

@pytest.fixture
def pim_page(page: Page):
    def pim_page_fync():
        with allure.step("Работа с модулем Personal Information Management"):
            page.goto(AUTH_URL)
            page.fill(USERNAME_INPUT, VALID_USERNAME)
            page.fill(PASSWORD_INPUT, VALID_PASSWORD)
            page.click(LOGIN_BUTTON)
            page.click(PIM_SECTION)
            page.click(ADD_EMPLOYEE)
            page.fill(FIRST_NAME, DATA_FIRST_NAME)
            page.fill(LAST_NAME, DATA_LAST_NAME)
            page.click(SAVE_BUTTON_1)
            expect(page.locator(STATUS_TEXT)).to_be_visible()
            page.click(PIM_SECTION)
            page.click(EMPLOYEE_LIST)
            page.wait_for_selector(SEARCH_NAME, state="visible")
            page.fill(SEARCH_NAME, DATA_EMPLOYEE, timeout=60000)
            page.click(SEARCH_BUTTON_1)
            page.click(DELETE_BUTTON, timeout=60000)
            page.click(CONFIRM_DELETE)

    return pim_page_fync

@pytest.fixture
def recruitment_page(page: Page):
    def recruitment_page_fync():
        with allure.step("Работа с модулем Recruitment"):
            page.click(RECRUITMENT_SECTION)
            page.click(VACANCIES_TAB)
            page.click(STATUS_DROPDOWN)
            page.wait_for_selector(STATUS_ACTIVE, timeout=30000)
            page.click(STATUS_ACTIVE)
            page.click(SEARCH_BUTTON_2)
            page.wait_for_timeout(3000)
            expect(page.locator(SEARCH_RESULTS_TABLE_ROW).first).to_be_visible()

    return recruitment_page_fync


@pytest.fixture
def admin_page(page: Page):
    def admin_page_fync():
        with allure.step("Работа с модулем Admin"):
            page.click(ADMIN_SECTION)
            page.click(CORPORATE_BRANDING)
            page.click(SOCIAL_BUTTON)
            page.click(PUBLISH_BUTTON)
            page.click(ADMIN_SECTION)
            page.click(NATIONAL_BUTTON)
            page.click(NATIONAL_OPTION)
            page.click(DELETE_OPTION)
            page.click(SELECTED_OPTION)
            expect(page.locator(ADMIN_SECTION)).to_be_visible()

    return admin_page_fync

@pytest.fixture
def buzz_page(page: Page):
    def buzz_page_fync():
        with allure.step("Работа с модулем Buzz"):
            page.click(BUZZ_SECTION)
            page.fill(NEWSFEED_TITLE, DATA_NEWSFEED)
            page.click(POST_BUTTON)
            page.click(BUZZ_SECTION)
            page.click(RECENT_POST_BUTTON)
            page.click(PROFILE_DROPDOWN)
            page.click(LOGOUT_LINK)
            expect(page.locator(USERNAME_INPUT)).to_be_visible()

    return buzz_page_fync








        






