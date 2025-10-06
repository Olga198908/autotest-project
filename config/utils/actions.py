from playwright.sync_api import Page
from config.logger import get_logger


class ActionPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def navigate(self, url):
        """Переходит на указанный URL"""
        self.logger.info(f"Переход по URL: {url}")
        self.page.goto(url)

    def click(self, locator, timeout=30000):
        """Кликает по элементу с заданным локатором"""
        self.logger.info(f"Клик по элементу: {locator}")
        self.page.click(locator, timeout=timeout)

    def fill(self, locator, text, timeout=30000):
        """Заполняет поле с заданным локатором текстом"""
        self.logger.info(f"Заполнение поля {locator} текстом: {text}")
        self.page.fill(locator, text, timeout=timeout)

    def wait_for_selector(self, locator, state="visible", timeout=30000):
        """Ждёт появления элемента с заданным локатором"""
        self.logger.info(f"Ожидание селектора {locator} (состояние: {state})")
        self.page.wait_for_selector(locator, state=state, timeout=timeout)

    def wait_for_timeout(self, milliseconds):
        """Ждёт указанное количество миллисекунд"""
        self.logger.info(f"Ожидание {milliseconds} мс")
        self.page.wait_for_timeout(milliseconds)

    def hover(self, locator):
        """Наводит курсор мыши на элемент"""
        self.logger.info(f"Наведение на элемент: {locator}")
        self.page.hover(locator)

    def get_text(self, locator):
        """Получает текстовое содержимое элемента"""
        text = self.page.text_content(locator)
        self.logger.info(f"Получен текст из {locator}: {text}")
        return text

    def is_visible(self, locator):
        """Проверяет, виден ли элемент на странице"""
        visible = self.page.is_visible(locator)
        self.logger.info(f"Элемент {locator} видим: {visible}")
        return visible

    def reload(self):
        """Перезагружает страницу"""
        self.logger.info("Перезагрузка страницы")
        self.page.reload()

    def keyboard_press(self, key):
        """Нажимает клавишу на клавиатуре"""
        self.logger.info(f"Нажатие клавиши: {key}")
        self.page.keyboard.press(key)

    def select_option_from_dropdown(self, dropdown_locator, option_text):
        """Выбирает опцию из выпадающего списка по тексту"""
        self.logger.info(f"Выбор опции '{option_text}' из dropdown {dropdown_locator}")
        self.click(dropdown_locator)
        self.wait_for_timeout(1000)
        option_locator = f".oxd-select-option:has-text('{option_text}')"
        self.click(option_locator)

    def fill_with_autocomplete(self, field_locator, text, select_first=True):
        """Заполняет поле с автодополнением и выбирает первый вариант"""
        self.logger.info(f"Заполнение поля с автодополнением {field_locator}")
        self.fill(field_locator, text)
        self.wait_for_timeout(2000)

        if select_first:
            self.keyboard_press("ArrowDown")
            self.keyboard_press("Enter")

    def wait_for_toast_message(self, timeout=30000):
        """Ждёт появления toast-сообщения"""
        self.logger.info("Ожидание toast-сообщения")
        self.wait_for_selector(".oxd-toast-container", timeout=timeout)

    def verify_element_visible(self, locator, element_name=""):
        """Проверяет что элемент видим и логирует результат"""
        is_visible = self.is_visible(locator)
        element_desc = element_name if element_name else locator
        if is_visible:
            self.logger.info(f"✓ Элемент '{element_desc}' видим")
        else:
            self.logger.warning(f"✗ Элемент '{element_desc}' не видим")
        return is_visible