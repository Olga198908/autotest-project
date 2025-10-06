import logging
import os
from datetime import datetime

# Определяем корневую директорию проекта
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(PROJECT_ROOT, "reports", "logs")
os.makedirs(LOG_DIR, exist_ok=True)


def get_logger(name: str = "orangehrm_tests"):
    """
    Создает и настраивает логгер для тестов OrangeHRM

    Args:
        name (str): Имя логгера, по умолчанию "orangehrm_tests"

    Returns:
        logging.Logger: Настроенный объект логгера
    """
    logger = logging.getLogger(name)

    # Если логгер уже настроен, возвращаем его
    if logger.hasHandlers():
        return logger

    # Устанавливаем уровень логирования
    logger.setLevel(logging.DEBUG)

    # Формат сообщений
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Файловый обработчик (все уровни)
    log_filename = f"orangehrm_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_file = os.path.join(LOG_DIR, log_filename)
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Консольный обработчик (только INFO и выше)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # Добавляем обработчики к логгеру
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Создаем основной логгер для быстрого использования
logger = get_logger("orangehrm_main")

if __name__ == "__main__":
    # Тестирование логгера
    logger.info("Логгер для OrangeHRM тестов успешно настроен")
    logger.debug("Отладочное сообщение")
    logger.warning("Тестовое предупреждение")
    logger.error("Тестовая ошибка")
    logger.info(f"Логи сохраняются в: {LOG_DIR}")