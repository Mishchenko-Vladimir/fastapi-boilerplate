# ![Логотип приложения](docs/assets/logo.png) FastAPI-Boilerplate
**FastAPI Boilerplate** — это продвинутый базовый шаблон для быстрой разработки асинхронных веб-приложений. 
Проект спроектирован как надежный фундамент, объединяющий лучшие практики **Clean Architecture** и современный технологический стек Python.

Этот шаблон избавляет от рутины по настройке авторизации, базы данных, админки и Docker-окружения, 
позволяя вам сосредоточиться на реализации бизнес-идей с первых минут.

## 🛠️ Технологический стек

| Компоненты                                                   | |
|--------------------------------------------------------------|---:|
| **🐍 Язык:** Python 3.14+                                    | [![Python](https://img.shields.io/badge/Python-3.14%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) |
| **⚡ Фреймворк:** FastAPI                                     | [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/) |
| **🚀 ASGI-сервер:** Uvicorn + Gunicorn                       | [![Uvicorn](https://img.shields.io/badge/Uvicorn-005571?style=for-the-badge&logo=fastapi&logoColor=white)](https://www.uvicorn.org/) [![Gunicorn](https://img.shields.io/badge/Gunicorn-F46D43?style=for-the-badge&logo=apache&logoColor=white)](https://gunicorn.org/) |
| **🗄️ База Данных:** PostgreSQL (asyncpg) + SQLite (aiosqlite) | [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/) [![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/) |
| **🔁 ORM:** SQLAlchemy (async)                               | [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-0B5566?style=for-the-badge&logo=python&logoColor=white)](https://www.sqlalchemy.org/) |
| **🔄 Миграции БД:** Alembic                                  | [![Alembic](https://img.shields.io/badge/Alembic-0B5566?style=for-the-badge&logo=python&logoColor=white)](https://alembic.sqlalchemy.org/) |
| **🔐 Аутентификация:** FastAPI-Users                         | [![FastAPI-Users](https://img.shields.io/badge/FastAPI--Users-005571?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi-users.github.io/fastapi-users/) |
| **🔧 Админка:** SQLAdmin                                     | [![SQLAdmin](https://img.shields.io/badge/SQLAdmin-0B5566?style=for-the-badge&logo=python&logoColor=white)](https://aminalaee.dev/sqladmin/) |
| **✅ Валидация:** Pydantic v2 + pydantic-settings             | [![Pydantic](https://img.shields.io/badge/Pydantic-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://docs.pydantic.dev/) [![pydantic--settings](https://img.shields.io/badge/pydantic--settings-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) |
| **🧩 Кэширование:** Redis + fastapi-cache2                   | [![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/) |
| **📄 Шаблонизация:** Jinja2                                  | [![Jinja2](https://img.shields.io/badge/Jinja2-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://jinja.palletsprojects.com/) |
| **🛡️ Защита:** slowapi + CORS                               | [![slowapi](https://img.shields.io/badge/slowapi-005571?style=for-the-badge&logo=fastapi&logoColor=white)](https://slowapi.readthedocs.io/) [![CORS](https://img.shields.io/badge/CORS-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://fastapi.tiangolo.com/tutorial/cors/) |
| **📧 Почта:** aiosmtplib                                     | [![aiosmtplib](https://img.shields.io/badge/aiosmtplib-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://aiosmtplib.readthedocs.io/) |
| **📦 Менеджер пакетов:** uv                                  | [![uv](https://img.shields.io/badge/uv-000000?style=for-the-badge&logo=python&logoColor=white)](https://docs.astral.sh/uv/) |
| **🐳 Контейнеризация:** Docker + Docker Compose              | [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/) [![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/compose/) |
| **🧪 Тестирование:** Pytest + httpx + faker                  | [![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/) [![HTTPX](https://img.shields.io/badge/HTTPX-0A9EDC?style=for-the-badge&logo=python&logoColor=white)](https://www.python-httpx.org/) [![Faker](https://img.shields.io/badge/Faker-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://faker.readthedocs.io/) |
| **📘 Документация:** OpenAPI (Swagger UI)                    | [![OpenAPI](https://img.shields.io/badge/OpenAPI-10985B?style=for-the-badge&logo=swagger&logoColor=white)](https://swagger.io/specification/) |
| **🧹 Форматирование кода:** Black                            | [![Black](https://img.shields.io/badge/Code%20Style-Black-000000?style=for-the-badge&logo=python&logoColor=white)](https://black.readthedocs.io/) |
| **📊 Покрытие тестами:** pytest-cov                          | [![pytest-cov](https://img.shields.io/badge/pytest--cov-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest-cov.readthedocs.io/) |

## 📂 Структура проекта

```bash
fastapi-boilerplate/
├── app/                         # Основной пакет приложения
│   ├── actions/                 # CLI-скрипты управления (создание суперпользователя и др.)
│   ├── admin/                   # Конфигурация админ-панели SQLAdmin
│   ├── alembic/                 # История и версии миграций базы данных
│   ├── api/                     # Слой сетевых интерфейсов (API)
│   │   ├── api_v1/              # Первая версия REST API эндпоинтов 
│   │   ├── dependencies/        # Инъекции зависимостей (Depends) для роутеров
│   │   ├── webhooks/            # Обработчики входящих уведомлений от внешних систем
│   │   └── __init__.py          # Агрегация и инициализация роутеров
│   ├── core/                    # Системное ядро и инфраструктурные компоненты
│   │   ├── auth/                # Конфигурация безопасности и логика fastapi-users
│   │   ├── cache/               # Настройки и утилиты кэширования (Redis)
│   │   ├── gunicorn/            # Конфигурация WSGI-сервера для продакшена
│   │   ├── config.py            # Валидация настроек через pydantic-settings (.env)
│   │   ├── db_helper.py         # Инициализация движка SQLAlchemy и сессий
│   │   ├── limiter.py           # Настройка ограничений частоты запросов (Rate Limiting)
│   │   └── templates.py         # Интеграция и конфигурация Jinja2Templates
│   ├── exceptions/              # Обработка исключений
│   │   ├── custom.py            # Определение пользовательских классов ошибок
│   │   └── handlers.py          # Глобальные обработчики исключений
│   ├── middleware/              # Кастомные middleware 
│   ├── models/                  # Описание сущностей базы данных (ORM SQLAlchemy)
│   ├── repositories/            # Слой доступа к данным (Data Access Layer)
│   │   └── crud_manager.py      # Универсальный CRUD-менеджер для работы с моделями
│   ├── schemas/                 # Модели данных Pydantic (DTO) для валидации и сериализации
│   ├── services/                # Слой бизнес-логики (UseCase Layer)
│   │   └── mailing/             # Почтовый сервис (рассылка уведомлений, подтверждений)
│   ├── static/                  # Статическое содержимое (CSS, JS, Изображения)
│   ├── templates/               # HTML-шаблоны (Jinja2)
│   ├── utils/                   # Вспомогательные функции общего назначения
│   │   └── case_converter.py    # Функция конвертации имени таблицы
│   ├── views/                   # Роутеры для рендеринга HTML-страниц (Frontend-интерфейс)
│   ├── .env                     # Переменные окружения (не отображается в git)
│   ├── .env.template            # Шаблон .env (автоматически заменяет .env, если его нет)
│   ├── alembic.ini              # Конфигурационный файл миграций Alembic              
│   ├── create_fastapi_app.py    # Фабрика для сборки и настройки экземпляра FastAPI         
│   ├── main.py                  # Точка входа для запуска в режиме разработки
│   ├── run.py                   # Запуск приложения через Gunicorn (для Docker)
│   └── run_main.py              # Создания и запуск приложения через Gunicorn
├── docker-build/                # Инфраструктурные файлы сборки
│   └── app/
│       ├── Dockerfile           # Инструкции для сборки Docker-образа
│       └── prestart.sh          # Скрипт подготовки БД (миграции + создание админа)
├── tests/                       # Пакет с автоматизированными тестами (Pytest)
├── docker-compose.yml           # Оркестрация контейнеров (App, DB, Redis, PGAdmin)
├── pyproject.toml               # Конфигурация проекта, зависимостей и инструментов (uv)
└── uv.lock                      # Фиксированные версии установленных пакетов
```