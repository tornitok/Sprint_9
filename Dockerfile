FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV BASE_URL=${BASE_URL:-https://foodgram-frontend-1.prakticum-team.ru/signin}
ENV SELENIUM_URL=${SELENIUM_URL:-http://selenoid:4444/wd/hub}
ENV USER_NAME=${USER_NAME:-Test_USer}
ENV PASSWORD=${PASSWORD:-09871234Link@}

RUN mkdir -p /app/allure-results

ENTRYPOINT ["pytest", "tests/", "-v", "--tb=short", "--alluredir=allure-results"]

