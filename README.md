# Продуктовый помощник — UI автотесты

Этот репозиторий содержит базовую структуру UI‑тестов для учебного проекта «Продуктовый помощник».

## Требования
- Python 3.11+
- Google Chrome (локально) или Selenium Grid (в CI)
- Зависимости из `requirements.txt`

## Установка и запуск (macOS, zsh)

```bash
cd /Users/klim/PycharmProjects/Sprint_9
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Установить URL приложения (если отличается)
export APP_BASE_URL="http://localhost:8000"

# Запуск тестов и сбор Allure результатов
pytest tests/ui --alluredir=allure-results
```

### Просмотр Allure отчёта локально
```bash
brew install allure
allure serve allure-results
```

## Переключение между локальным Chrome и удалённым Selenium

Фикстуры поддерживают Remote WebDriver через переменную окружения `SELENOID_URL`:

```bash
# Локально, хедлесс
export HEADLESS=1
pytest tests/ui -q --alluredir=allure-results

# Против удалённого Selenium Grid / Selenoid
export SELENOID_URL="http://localhost:4444/wd/hub"
pytest tests/ui -q --alluredir=allure-results
```

## Локальный Selenoid (опционально)

В репозитории добавлен `docker-compose.selenium.yml` и `selenoid/browser.json`.

1. Убедись, что установлен Docker Desktop.
2. Подними Selenoid и UI:

```bash
docker compose -f docker-compose.selenium.yml up -d
```

3. Проверь UI по адресу http://localhost:8080.
4. Запусти тесты против Selenoid:

```bash
pytest tests/ui --base-url "http://localhost:8000" --remote-url "http://localhost:4444/wd/hub" --headless 1 --alluredir=allure-results
```

Если нужен другой образ/версия браузера — отредактируй `selenoid/browser.json` согласно документации Selenoid.

## Структура тестов
- `tests/ui/test_registration.py` — сценарий «Создание аккаунта».
- `tests/ui/pages/registration_page.py` — PageObject для регистрации.
- `tests/ui/utils/paths.py` — работа с Pathlib и каталогом `assets`.
- `tests/ui/assets/` — тестовые файлы для загрузки.

## CI — GitHub Actions
Workflow `.github/workflows/ui-tests.yml`:
- Поднимает сервис Selenium (standalone-chrome)
- Устанавливает Python и зависимости
- Запускает pytest с Allure
- Сохраняет `allure-results` как артефакт

Для работы тестов в CI нужно указать переменную `APP_BASE_URL` в GitHub Actions Variables (в настройках репозитория).
