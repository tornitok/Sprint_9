#!/bin/bash

# Скрипт для запуска тестов Foodgram с Selenoid

set -e

echo "🚀 Foodgram UI Tests Automation"
echo "================================"
echo ""

# Проверка наличия Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker не установлен. Пожалуйста, установите Docker."
    exit 1
fi

# Проверка наличия Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose не установлен. Пожалуйста, установите Docker Compose."
    exit 1
fi

# Стартовые опции
case "${1:-run}" in
    start)
        echo "🐳 Запуск Selenoid..."
        docker-compose up -d
        echo "✅ Selenoid запущен!"
        echo "   WebDriver API: http://localhost:4444/wd/hub"
        echo "   UI консоль: http://localhost:8080"
        ;;

    stop)
        echo "🛑 Остановка Selenoid..."
        docker-compose down
        echo "✅ Selenoid остановлен!"
        ;;

    run)
        echo "🧪 Запуск тестов..."
        echo ""

        # Проверка, запущен ли Selenoid
        if ! curl -s http://localhost:4444/wd/hub/status > /dev/null 2>&1; then
            echo "⚠️  Selenoid не запущен. Запускаю..."
            docker-compose up -d
            sleep 3
        fi

        # Запуск тестов
        python -m pytest tests/ -v --alluredir=allure-results
        echo ""
        echo "✅ Тесты завершены!"
        ;;

    report)
        echo "📊 Открытие отчёта Allure..."
        allure serve allure-results
        ;;

    logs)
        echo "📋 Логи Selenoid:"
        docker-compose logs -f selenoid
        ;;

    *)
        echo "Usage: $0 {start|stop|run|report|logs}"
        echo ""
        echo "Commands:"
        echo "  start   - Запустить Selenoid"
        echo "  stop    - Остановить Selenoid"
        echo "  run     - Запустить тесты (запустит Selenoid если он не запущен)"
        echo "  report  - Открыть отчёт Allure"
        echo "  logs    - Показать логи Selenoid"
        exit 1
        ;;
esac

