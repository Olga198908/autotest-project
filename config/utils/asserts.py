from playwright.sync_api import Page
from config.logger import get_logger


class AssertPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def url_contains(self, expected_url_part: str):
        # Проверяет, что текущий URL страницы содержит ожидаемую часть
        actual_url = self.page.url
        assert expected_url_part in actual_url, f"URL должен содержать: {expected_url_part}, текущий URL: {actual_url}"
        self.logger.info(f"URL содержит ожидаемую часть: {expected_url_part}")

    def element_is_visible(self, locator: str):
        # Проверяет, что элемент отображается на странице
        assert self.page.is_visible(locator), f"Элемент {locator} должен быть видим"
        self.logger.info(f"Элемент {locator} видим на странице")

    def element_is_hidden(self, locator: str):
        # Проверяет, что элемент скрыт
        assert self.page.is_hidden(locator), f"Элемент {locator} должен быть скрыт"
        self.logger.info(f"Элемент {locator} скрыт на странице")

    def element_contains_text(self, locator: str, expected_text: str):
        # Проверяет, что элемент содержит указанный текст
        actual_text = self.page.text_content(locator)
        assert expected_text in (actual_text or ""), f"Элемент {locator} не содержит текст: {expected_text}"
        self.logger.info(f"Элемент {locator} содержит текст: {expected_text}")

    def element_text_is(self, locator: str, expected_text: str):
        # Проверяет, что текст элемента полностью соответствует ожидаемому
        actual_text = self.page.text_content(locator)
        assert actual_text == expected_text, f"Ожидали текст '{expected_text}', получили: '{actual_text}'"
        self.logger.info(f"Текст элемента {locator} точно соответствует: {expected_text}")

    def element_is_enabled(self, locator: str):
        # Проверяет, что элемент активен
        assert self.page.is_enabled(locator), f"Элемент {locator} должен быть активен"
        self.logger.info(f"Элемент {locator} активен")

    def element_is_disabled(self, locator: str):
        # Проверяет, что элемент отключён
        assert not self.page.is_enabled(locator), f"Элемент {locator} должен быть отключён"
        self.logger.info(f"Элемент {locator} отключён")

    def element_count_is(self, locator: str, expected_count: int):
        # Проверяет, что количество найденных элементов совпадает с ожидаемым
        count = self.page.locator(locator).count()
        assert count == expected_count, f"Ожидали {expected_count} элементов {locator}, получили: {count}"
        self.logger.info(f"Найдено {count} элементов {locator} (ожидалось: {expected_count})")

    def element_has_class(self, locator: str, class_name: str):
        # Проверяет, что элемент содержит указанный CSS класс
        classes = self.page.get_attribute(locator, "class") or ""
        assert class_name in classes.split(), f"Элемент {locator} не содержит класс: {class_name}"
        self.logger.info(f"Элемент {locator} содержит класс: {class_name}")

    def toast_message_is_visible(self):
        # Проверяет, что toast-сообщение отображается
        assert self.page.is_visible(".oxd-toast-container"), "Toast-сообщение должно быть видимым"
        self.logger.info("Toast-сообщение отображается")

    def table_has_rows(self, table_locator: str = ".oxd-table-row"):
        # Проверяет, что таблица содержит хотя бы одну строку
        count = self.page.locator(table_locator).count()
        assert count > 0, f"Таблица должна содержать строки, найдено: {count}"
        self.logger.info(f"Таблица содержит {count} строк")

    def success_message_displayed(self):
        # Проверяет, что отображается сообщение об успешном выполнении
        assert self.page.is_visible(".oxd-toast-container"), "Сообщение об успехе должно отображаться"
        self.logger.info("Сообщение об успешном выполнении отображается")

    def login_successful(self):
        # Проверяет, что логин выполнен успешно (по наличию дашборда)
        assert self.page.is_visible(".oxd-brand-banner"), "Логин не выполнен - дашборд не отображается"
        self.logger.info("Логин выполнен успешно")

    def employee_created_successfully(self):
        # Проверяет, что сотрудник создан успешно
        assert self.page.is_visible(".oxd-toast-container"), "Сотрудник не создан - нет сообщения об успехе"
        self.logger.info("Сотрудник создан успешно")

    def vacancy_created_successfully(self):
        # Проверяет, что вакансия создана успешно
        assert self.page.is_visible(".oxd-toast-container"), "Вакансия не создана - нет сообщения об успехе"
        self.logger.info("Вакансия создана успешно")

    def search_results_displayed(self):
        # Проверяет, что результаты поиска отображаются
        assert self.page.is_visible(".oxd-table-row"), "Результаты поиска не отображаются"
        self.logger.info("Результаты поиска отображаются")

    def element_exists_in_dom(self, locator: str):
        # Проверяет, что элемент существует в DOM
        count = self.page.locator(locator).count()
        assert count > 0, f"Элемент {locator} не найден в DOM"
        self.logger.info(f"Элемент {locator} существует в DOM")

    def page_title_contains(self, expected_title_part: str):
        # Проверяет, что заголовок страницы содержит ожидаемую часть
        actual_title = self.page.title()
        assert expected_title_part in actual_title, f"Заголовок должен содержать: {expected_title_part}, текущий: {actual_title}"
        self.logger.info(f"Заголовок страницы содержит: {expected_title_part}")