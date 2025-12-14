.PHONY: install start stop run report logs clean help

help:
	@echo "Foodgram UI Tests - Доступные команды"
	@echo "======================================"
	@echo ""
	@echo "make install  - Установить зависимости"
	@echo "make start    - Запустить Selenoid"
	@echo "make stop     - Остановить Selenoid"
	@echo "make run      - Запустить все тесты"
	@echo "make report   - Открыть Allure отчёт"
	@echo "make logs     - Показать логи Selenoid"
	@echo "make clean    - Очистить кэш и результаты"
	@echo ""

install:
	@echo "📦 Установка зависимостей..."
	pip install -r requirements.txt
	@echo "✅ Зависимости установлены!"

start:
	@echo "🐳 Запуск Selenoid..."
	docker-compose up -d
	@echo "✅ Selenoid запущен!"
	@echo "   WebDriver API: http://localhost:4444/wd/hub"
	@echo "   UI консоль: http://localhost:8080"

stop:
	@echo "🛑 Остановка Selenoid..."
	docker-compose down
	@echo "✅ Selenoid остановлен!"

run: start
	@echo "🧪 Запуск тестов..."
	python -m pytest tests/ -v --alluredir=allure-results
	@echo ""
	@echo "✅ Тесты завершены!"
	@echo "Используйте 'make report' для просмотра отчёта"

report:
	@echo "📊 Открытие отчёта Allure..."
	allure serve allure-results

logs:
	@echo "📋 Логи Selenoid:"
	docker-compose logs -f selenoid

clean:
	@echo "🧹 Очистка кэша и результатов..."
	rm -rf __pycache__ .pytest_cache allure-results
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "✅ Проект очищен!"

