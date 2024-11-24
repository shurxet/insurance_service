
# Проект по расчёту страховой стоимости

Это проект состоит из бэкенда на FastAPI и фронтенда на React (с Vite). Проект поддерживает работу с базой данных PostgreSQL и миграции с использованием Alembic. Для удобства развертывания используется Docker.

---

## Содержание

1. [Функции](#функции)  
2. [Используемые технологии](#используемые-технологии)  
3. [Установка](#установка)  
4. [Конфигурация](#конфигурация)  
5. [Запуск приложения](#запуск-приложения)  
6. [Миграции базы данных](#миграции-базы-данных)  
7. [API-эндпоинты](#api-эндпоинты)  
8. [Тестирование](#тестирование)  
9. [Участие в разработке](#участие-в-разработке)  
10. [Лицензия](#лицензия)

---

## Функции

- **Бэкенд**: REST API с FastAPI.  
- **Фронтенд**: Веб-интерфейс на React с Vite.  
- **База данных**: PostgreSQL.  
- **Миграции**: Управление с помощью Alembic.  
- **Докеризация**: Полная поддержка Docker для фронтенда, бэкенда и базы данных.  
- **Проверка готовности**: Healthcheck для базы данных и бэкенда.  

---

## Используемые технологии

- [FastAPI](https://fastapi.tiangolo.com/)  
- [React](https://react.dev/)  
- [Vite](https://vitejs.dev/)  
- [PostgreSQL](https://www.postgresql.org/)  
- [Alembic](https://alembic.sqlalchemy.org/)  
- [Docker](https://www.docker.com/)  
- [Poetry](https://python-poetry.org/)  
- [Pydantic](https://pydantic-docs.helpmanual.io/)
---

## Установка

### 1. Клонирование репозитория:

```bash
git clone https://github.com/shurxet/insurance_service.git
cd insurance_service
```

---

### 2. Создание `.env` файлов:

#### Бэкенд (`docker/develop/.env`):
```env
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=dbname
POSTGRES_HOST=db
POSTGRES_PORT=5432

```

## Конфигурация

Бэкенд и фронтенд используют переменные окружения для конфигурации. Убедитесь, что вы настроили `.env` файлы правильно (см. [Установка](#установка)).

---

## Запуск приложения

Создание файла .env
Для успешного запуска контейнеров необходимо создать файл .env в корневой директории проекта. Этот файл должен содержать следующие переменные окружения:

POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=dbname
POSTGRES_HOST=db
POSTGRES_PORT=5432

Проект использует Docker для развертывания. Все сервисы можно запустить одной командой:


```bash
docker-compose up -d --build
```

После запуска:

- **Фронтенд**: [http://localhost](http://localhost:3000)  
- **Бэкенд**: [http://localhost:8000](http://localhost:8000)

---

## Миграции базы данных

Для управления миграциями используется Alembic.

- **Запуск миграций**:
  ```bash
  docker-compose run backend alembic upgrade head
  ```
- **Создание новой миграции**:
  ```bash
  docker-compose run back alembic revision --autogenerate -m "Ваше сообщение о миграции"
  ```

---

## API-эндпоинты

- **POST /insurance**: Расчитать страховку.

- **POST /rate**: Добавить тариф.

- **GET /rate**: Получить список тарифов.  
- **POST /rate**: Добавить тариф.  
- **GET /rate/{id}**: Получить тариф по ID.  
- **PUT /rate/{id}**: Обновить тариф по ID.
- **DELETE /rate/{id}**: Удалить тариф по ID.

- **GET /cargo**: Получить список грузов.  
- **POST /stores**: Добавить груз.  
- **GET /stores/{id}**: Получить груз по ID.  
- **PUT /stores/{id}**: Обновить груз по ID.

---

## Участие в разработке

Если вы хотите внести свой вклад, клонируйте репозиторий, создайте ветку и отправьте PR.

---

## Лицензия

Этот проект доступен под лицензией MIT.

---
