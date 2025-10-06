# 📝 Markdown Разметка — Шпаргалка
- Справочник по основным синтаксическим элементам Markdown с примерами.
- [Инструкция](https://doka.guide/tools/markdown/)
> - [Онлайн редактор](https://markdown-editor.github.io/)
> - [Онлайн редактор Dillinger](https://dillinger.io/)
> - [Десктоп редактор Typora](https://typora.io/)

## 🔤 Текст

### Заголовки

```markdown

# Заголовок H1
## Заголовок H2
### Заголовок H3
#### Заголовок H4
##### Заголовок H5
###### Заголовок H6

Альтернативный стиль (Только H1 и H2):

Заголовок H1
===

Заголовок H2
---

```

### Форматирование

```markdown

*Курсив* или _Курсив_
**Жирный** или __Жирный__
***Жирный курсив*** или ___Жирный курсив___
~~Зачеркнутый~~
==Выделенный текст==
`Встроенный код`
```

## 📦 Блоки

### Цитаты

```markdown

> Основная цитата
>> Вложенная цитата
> 
> Цитата с **форматированием**

```

### Код

```markdown

Просто код:
    ```
    print("Hello World!")
    ```
Код конкретного языка, например пайтон:
    ```python
    def hello():
        print("Hello World!")
    ```
Код команд терминала:
    ```bash
    # Команды терминала
    $ npm install
    ```

```

### Горизонтальные линии (разделители)

```markdown

---
***
___

```

## 📌 Списки
- Менять вложенность пунктов можно через клавишу ТАБ, отменять ШИФТ+ТАБ

### Нумерованные

```markdown

1. Первый пункт
2. Второй пункт
   1. Вложенный (Tab)
   2. Вложенный
3. Третий пункт (Shift+Tab)

```

### Маркированные

```markdown

- Основной уровень
  * Второй уровень (Tab)
    + Третий уровень
  * Возврат (Shift+Tab)

```

### Чек-листы

```markdown

- [x] Выполнено
- [ ] Не выполнено
  - [ ] Подзадача

```

## 📊 Таблицы

```markdown

|Заголовок|Выравнивание|Выравнивание|Выравнивание|
|---|:---|---:|:---:|
|Данные|Лево|Право|Центр|
|*Курсив*|`Код`|```Код```|[ИМЯ ССЫЛКИ](https://ССЫЛКА)|

```
[Генератор таблиц](https://www.tablesgenerator.com/markdown_tables)

## 🎨 Дополнительно

### Экранирование
\*Экранированный символ\*

### Спойлер (HTML)
<details>
<summary>Спойлер</summary>
Скрытый текст
</details>

### 🔗 Ссылки
```markdown
[Текст ссылки](https://ссылка.ru)
Можно добавить подсказку:
[Текст ссылки](https://ссылка.ru "Всплывающая подсказка")
Можно просто ссылку сделать:
<https://ссылка.ru>
```

### 🎨 Изображения
```markdown
![Альтернативный текст](image.jpg "Подсказка")
Или HTML:
<img src="image.jpg" alt="Подсказка" width="200">
```

### Комментарии (не отображаются)
```markdown
<!-- Это комментарий, который не будет отображаться в рендере -->
```

## ⚡ HTML-элементы
- Безопасность: Избегайте <script>, <iframe> с ненадежными источниками
- Поддержка: Проверяйте рендеринг на вашей платформе (GitHub/GitLab/etc)
- Доступность: Всегда добавляйте alt для изображений (описание)
- Адаптивность: Используйте относительные размеры (width="100%")

### Текст и форматирование
```markdown
Подсветка текста:
<mark>Выделенный текст</mark>

Верхний/нижний индекс:
H<sub>2</sub>O и E=mc<sup>2</sup>

Комбинации клавиш:
Нажмите <kbd>Ctrl</kbd> + <kbd>C</kbd>

Время:
<time datetime="2023-10-05">5 октября</time>

```

### Интерактивные элементы
```markdown
Детали/спойлер:
<details>
  <summary>Показать ответ</summary>
  <p>Скрытое содержимое с <strong>форматированием</strong></p>
</details>

В одну строку:
<details><summary>Показать</summary><p>Содержимое</p></details>

Кнопки:
<button onclick="alert('Clicked!')">Нажми меня</button>

Детали/спойлер кнопкой:
<button onclick="alert('Clicked!')">
<details><summary>Показать</summary><p>
Содержимое
</p></details>
</button>

Прогресс-бар:
<progress value="75" max="100"></progress>

```

### Медиа-элементы
```markdown
Изображение с контролем размера:
<img src="image.jpg" alt="Описание" width="300" height="200">

Аудио:
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
</audio>

Видео с постером:
<video controls width="500" poster="preview.jpg">
  <source src="video.mp4" type="video/mp4">
</video>

YouTube (iframe):
<iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" frameborder="0" allowfullscreen></iframe>

```

### Навигация и организация
```markdown
Якорные ссылки:
<a href="#section-id">Перейти к разделу</a>

Горизонтальный скролл для широких блоков:
<div style="overflow-x: auto;">
  <table>...</table>
</div>

Разделитель с CSS:
<div style="height: 1px; background: #eee; margin: 20px 0;"></div>
```

### Специальные элементы
```markdown
Инструмент для копирования:
<pre><code id="code-block">npm install package</code></pre>
<button onclick="navigator.clipboard.writeText(document.getElementById('code-block').innerText)">
  Копировать
</button>

Кастомные атрибуты:
<div data-info="custom-data">Элемент с данными</div>

Сворачиваемый блок с CSS:
<div style="cursor: pointer;" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'none' ? 'block' : 'none'">
  ▽ Заголовок
</div>
<div style="display: none;">
  Скрытое содержимое
</div>
```

### Безопасные SVG (для логотипов/иконок)
```markdown
<svg height="20" width="20" viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="10" fill="#4285F4"/>
</svg>
```

# Пример README.md
# qa-edu
Тестовый проект автоматизации на Python с использованием:
- 🖥️ Selenium/Playwright (UI)
  - ✅ Дымовые тесты
  - ✅ Приемочные тесты
- 📊 Нагрузочное тестирование (Locust)

## 🧪 Модули и тест-кейсы
- Покрыты модули:
  - Авторизация
  - Страница товаров

<details><summary>Тестовые случаи</summary><p>

### Модуль авторизации
| ID  | Название       | Действия                     | Ожидаемый результат       |
|-----|----------------|------------------------------|---------------------------|
| TC1 | Успешный логин | Ввод валидных credentials    | Редирект в личный кабинет |
| TC2 | Выход          | Клик по кнопке "Выйти"       | Сессия завершена          |

### Модуль товаров
| ID  | Название            | Действия                     | Ожидаемый результат        |
|-----|---------------------|------------------------------|----------------------------|
| TC3 | Добавление товара   | Клик по кнопке "Добавить"    | Товар появляется в корзине |
| TC4 | Удаление товара     | Клик по кнопке "Удалить"     | Товар исчезает из корзины  |
</p></details>

## Архитектура проекта
<details><summary>Структура директорий</summary><p>

```
qa-edu/
├── tests/
│ ├── smoke/                # Дымовые тесты
│ ├── regression/           # Приемочные тесты
│ └── performance/          # Нагрузочные тесты
├── pages/
│ ├── login_out_page.py     # Страницы авторизации
│ ├── market_page.py        # Страницы товаров
│ ├── data.py               # Тестовые данные
│ └── locators.py           # Локаторы элементов
├── utils/
│ ├── actions.py            # Основные функции
│ └── helpers.py            # Вспомогательные функции
├── config/
│ ├── conftest.py           # Фикстуры pytest
│ └── settings.py           # Настройки проекта
├── run.py                  # Файл запуска тестов
├── requirements.txt        # Зависимости
├── pytest.ini              # Конфигурация pytest
└── README.md               # Документация
```
</p></details>

## Запуск
Как запустить тесты:
```bash
# Все тесты
pytest tests/

# С конкретными параметрами
pytest tests/smoke/ -v --html=report.html
```
## Зависимости
```bash
pip install -r requirements.txt
```
- Основные пакеты:
> - pytest==7.4.0
> - selenium==4.10.0
> - allure-pytest==2.13.2