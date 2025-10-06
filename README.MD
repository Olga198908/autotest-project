# **Шаблон автоматизированного тестирования** 
* Учебный проект (и шаблон) простой автоматизации труда ручного тестирования.
* Основной функционал - UI скрипты на `python` с использованием библиотеки `playwright` и `pytest`
* Тестируется демо-версия [OrangeHRM](https://opensource-demo.orangehrmlive.com/)
 
## Подготовка:

<details>
<summary>
==[НАЖМИ]== Ссылки на скачивание и инструкции по настройке среды разработки
</summary><p>

* [Скачать `Python` версии 13+](https://www.python.org/downloads/)
  * [Инструкция установки `Python` глава 2.1, эксплуатация глава 3](https://disk.yandex.ru/edit/d/ziggIjO2lsG0H2023WbIniPegnqahzm72s0qoIz-cKg6UlFmWEZta1prdw)
* [Скачать `git` версии 2.49+](https://git-scm.com/downloads)
  * [Инструкция установки и эксплуатации `git` глава 4.5](https://disk.yandex.ru/i/p6A-v9AiGy5qxA)
* IDE:
  * `OpenIDE` - Российский IDE
    * [Скачать версии 243+](https://openide.ru/download/)
  * `PyCharm` - Рекомендуемый способ взаимодействия с `python`
    * [Скачать версии Community Edition 2024+](https://www.jetbrains.com/ru-ru/pycharm/download/other.html)
    * [Установка глава 2.2 | Эксплуатация глава 4](https://disk.yandex.ru/edit/d/ziggIjO2lsG0H2023WbIniPegnqahzm72s0qoIz-cKg6UlFmWEZta1prdw)
  * `VSCode` - Популярный IDE
    * [Скачать версии 1.99+](https://code.visualstudio.com/docs/?dv=win64user)
</p></details>

## **Требования к запуску**
* Описаны в файле `requirements.txt`
* Установка требований из этого файла:
```shell
pip install -r requirements.txt
```
* Альтернативная установка требований:
```shell
pip install playwright pytest pytest-playwright pytest-html allure-pytest requests locust faker
```
* После установки пакетов, установите браузера `playwright`, этой командой установятся 3 (firefox, chromium, webkit) браузера:
```shell
playwright install
```
* Можно указать конкретный браузер (ещё есть msedge, разные версии и прочее) и другие команды:
```shell
playwright install firefox                              # Установить конкретный браузер последней версии
playwright install chromium --channel=chrome-beta       # Установить определенную версию
playwright install --dry-run                            # Показать список установленных браузеров
playwright install --with-deps                          # Установить браузеры для CI (надо sudo)
playwright uninstall chromium                           # Удалить браузер
```

## **Запуск авто-тестов**
* Запуск тестов через `pytest`:
```shell
# Запуск скриптов:
pytest                                              # запустит все фикстуры @pytest в проекте\директории
pytest ПУТЬ/К                                       # запустит все фикстуры @pytest в указанной папке
pytest ПУТЬ/К/ФАЙЛА.py                              # запуск файла с тестами
pytest ПУТЬ/К/ФАЙЛА.py::КЛАСС                       # запуск класса в файле с тестами
pytest ПУТЬ/К/ФАЙЛА.py::КЛАСС::МЕТОД                # запуск метода класса в файле с тестами
# Параметры запуска:
pytest -m smoke # Запуск всех тестов с маркой, т.е. тесты помеченные фикстурой `@pytest.mark.smoke` + регистрация в `pytest.ini` в `markers =`
pytest -m "smoke and regression"                    # Запуск тестов с двумя марками
pytest -m "smoke or regression"                     # Логическое "или"
pytest -m "not slow"                                # Запуск тестов без метки slow
pytest --browser=firefox                            # выбор браузера (chromium, webkit) (если описаны в pytest.ini)
pytest --headless                                   # скрыть браузер (если описаны в pytest.ini)
pytest -k "name"                                    # пуск тестов содержащие в имени введённый текст
pytest -n 4                                         # пуск тестов параллельно (потоки процессора)
pytest --alluredir=reports/allure-results           # пуск тестов с формированием отчета allure (без генерации)
# Прочие параметры запуска:
pytest -v                                           # Подробный вывод (verbose)
pytest -s                                           # Отключить перехват вывода stdout/stderr, полезно для print()
pytest --tb=short                                   # Короткий трейсбек при падении теста
pytest --maxfail=2                                  # Остановиться после 2 падений
pytest --capture=tee-sys                            # Показывать вывод print() и сохранять его
pytest --disable-warnings                           # Отключить предупреждения
pytest --lf                                         # Запустить только упавшие в прошлый раз
pytest --ff                                         # Сначала упавшие, потом остальные
pytest --durations=2                                # Показать (в конце лога итогов прогона) 2 самых медленных теста
# Пример полной команды:
pytest tests/smoke/test_smoke_orange.py::test_flow --browser=chromium --headless --alluredir=allure-results -v
```

## **Allure отчеты**

Для генерации и просмотра детальных отчетов о выполнении тестов используется Allure Framework.

### **Быстрый старт**

```bash
# 1. Запуск тестов с генерацией данных для Allure
pytest tests/smoke/test_smoke_orange.py --alluredir=allure-results

# 2. Просмотр отчета в браузере
allure serve allure-results
```

### **Генерация статического отчета**

```bash
# Генерация HTML отчета
allure generate allure-results -o allure-report --clean

# Открытие отчета
open allure-report/index.html
```shell
# Убедитесь в нахождении или перейдите командой CD в главную директорию проекта
# Запустите генерацию отчётов из сырых данных в allure-results, в готовые в allure-report
# ИЛИ Команда генерации + запуск + удаление
allure serve reports/allure-results
```

## **Покрытые авто-тестами модули**
* **Авторизация** - `pages/base_page.py`
* **Управление персоналом** - `page/base_page.py`
* **Управление вакансиями** - `page/base_page.py`
* **Администрирование** - `page/base_page.py`
* **взаимодействие** - `page/base_page.py`

## **Архитектура проекта**
<details>
<summary>
==[НАЖМИ]== Структура директорий
</summary><p>

```
/Autotest-Project/                  # корневой каталог (репозиторий) проекта авто-тестов
├── /pages/                          # page object модели│ 
│   ├── base_page.py                # базовый page object класс (основные методы работы со страницей)
│   └── __init__.py
├── /test/                          # тестовые сценарии с группировкой по видам
│   ├── /smoke/                     # дымы (фронт)
│   │  ├── __int__.py   
│   │  └── test_smoke_orange.py
│   ├── /accept/                    # приемка (фронт)
│   │ 
│   ├── /api/                       # апи (бэк)
│   │   └── orange_playwright_api.py
│   ├── /load/                      # нагрузочное (locust)
│   │   ├── locust_orange.py
│   │   └── __init__.py 
│   ├── __init__.py  
│   └── conftest.py             # фикстуры pytest для конфигурации тестов и отчетности allure
├── /config/                        
│   ├── /utils/                     
│   │   ├── actions.py              # действия
│   │   ├── asserts.py              # проверки
│   │   └── __init__.py
│   ├── logger.py                   # конфигурация логирования
│   └── __init__.py
├── /report/                        # отчеты и артефакты (хранятся локально, должно быть подключено хранение в jenkins)
│   └── /logs/                      # логи выполнения тестов (pytest cli)
│         └── pytest_execution.log   
├── /docs/                          # документация
│   ├── PLAN.md                     # документация проекта, план автоматизации, тест-кейсы и история изменений
│   ├── ALLURE.md                   # описывает, как работать с отчетами Allure в проекте (как их генерировать, просматривать)
│   ├── CODE.md                     # описание стиля кода в проекте
│   ├── ARCH.md                     # описание вариантов архитектур проекта
│   ├── MD.md                       # описание markdown разметки
│   ├── IDE.md                      # описание работы в различных IDE и их настройки
│   ├── TERMINAL.md                 # описание работы в различных терминалах (cmd\unix\bash)
│   ├── PW.md                       # документация по использованию фреймворка Playwright
│   ├── PYTHON.md                   # документация по работе с Python
│   └── GIT.md                      # описание работы с git и bitbucket
├── pytest.ini                      # настройки pytest
├── runner.py                       # запускатор для тестовых прогонов
├── requirements.txt                # зависимости
├── README.md                       # описание проекта
└── .gitignore                      # игнор лист git
```
</p></details>

* Отчеты и артефакты папки `report` только для локального хранения, в эксплуатации подразумевается хранение артефактов в `jenkins`.
* Подробнее описано в файле `ARCH.md` в папке `docs` в корневой директории проекта

## **Работа в репозитории**
* **Пример безопасного workflow в `git`**
```shell
# Перед началом работы
git pull origin main

# После нужных изменений и ревью сформируйте инlекс
git add .

# Проверить, что нет лишних файлов
git status

# Создание коммита
git commit -m "Комментарий"

# Отправка изменений на сервер (-u чтобы запомнил ветки, потом можно просто git push)
git push -u origin main
```
* **Подключение к репозиторию через `git`** описано в [docs \ `ALLURE.md`](https://github.com/Olga198908/autotest-project/blob/main/docs/GIT.md)