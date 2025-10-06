import pytest
import allure
from playwright.sync_api import sync_playwright, Page
from pages.base_page import *

@allure.title("End-to-End тест основных модулей OrangeHRM")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_flow(page, auth_login, pim_page, recruitment_page, admin_page, buzz_page):
    with allure.step("Выполнение полного потока тестирования"):
        auth_login()
        pim_page()
        recruitment_page()
        admin_page()
        buzz_page()