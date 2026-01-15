import logging
import os

from typing import Literal
from pathlib import Path
from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


# Получаем путь до корневой директории проекта
# ...\fastapi-boilerplate\app\
BASE_DIR = Path(__file__).resolve().parent.parent

# Формат логирования
LOG_DEFAULT_FORMAT = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)


class RunConfig(BaseModel):
    """Конфигурация запуска"""

    host: str = "127.0.0.1"
    port: int = 8000


class GunicornConfig(BaseModel):
    """Конфигурация запуска через gunicorn"""

    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 1
    timeout: int = 900


class LoggingConfig(BaseModel):
    """Конфигурация логирования"""

    log_level: Literal[
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ] = "info"
    log_format: str = LOG_DEFAULT_FORMAT

    @property
    def log_level_value(self) -> int:
        return logging.getLevelNamesMapping()[self.log_level.upper()]


class ViewPrefix(BaseModel):
    """Конфигурация префикса для страниц"""

    pass


class ApiV1Prefix(BaseModel):
    """Конфигурация префикса API версии 1"""

    prefix: str = "/v1"
    auth: str = "/auth"
    users: str = "/users"


class ApiPrefix(BaseModel):
    """Конфигурация префикса API"""

    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()

    cookie_max_age: int = 3600  # время жизни куки в секундах

    # Автоматическое определение на основе переменной окружения (True - только для HTTPS, False - для HTTP)
    # В Docker (ENVIRONMENT=production uvicorn main:app --host 0.0.0.0 --port 8000)
    cookie_secure: bool = os.getenv("ENVIRONMENT") == "production"

    # Список разрешенных доменов для кросс-доменных запросов (сайты с которых можно отправлять запросы на наш API)
    allowed_origins: list[str] = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:1080",
        "http://localhost:1025",
    ]

    @property
    def bearer_token_url(self) -> str:
        # api/v1/auth/login
        parts = (self.prefix, self.v1.prefix, self.v1.auth, "/login")
        path = "".join(parts)
        return path.removeprefix("/")  # Удаляем начальный /


class DataBaseConfig(BaseModel):
    """Подключение к базе данных"""

    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class WebhookConfig(BaseModel):
    """Конфигурация вебхука, для отправки сообщений"""

    # Куда будут отправляться сообщения
    webhook_url: str


class AdminConfig(BaseModel):
    """Конфигурация администратора"""

    # True - Публичная форма аутентификации для администратора
    # False - SQLAdmin форма аутентификации
    public_auth: bool = True

    admin_email: str
    admin_password: str


class RateLimitConfig(BaseModel):
    """Конфигурация ограничения частоты запросов (rate limiting)"""

    enabled: bool = True
    default_limits: list[str] = ["100/minute"]


class AccessToken(BaseModel):
    """Настройки токена"""

    # Срок жизни токена
    lifetime_seconds: int = 3600

    reset_password_token_secret: str
    verification_token_secret: str


class RedisDB(BaseModel):
    """Настройки Redis"""

    cache: int = 0


class RedisConfig(BaseModel):
    """Настройки Redis"""

    host: str = "localhost"
    port: int = 6379
    db: RedisDB = RedisDB()


class CacheNamespace(BaseModel):
    """Именование пространства кэша"""

    users_list: str = "users-list"


class CacheConfig(BaseModel):
    """Настройки кэша"""

    enabled: bool = True
    prefix: str = "fastapi-cache"
    namespace: CacheNamespace = CacheNamespace()


class Settings(BaseSettings):
    """Настройка приложения"""

    model_config = SettingsConfigDict(
        env_file=(BASE_DIR / ".env.template", BASE_DIR / ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()
    gunicorn: GunicornConfig = GunicornConfig()
    logging: LoggingConfig = LoggingConfig()
    api: ApiPrefix = ApiPrefix()
    view: ViewPrefix = ViewPrefix()
    db: DataBaseConfig
    access_token: AccessToken
    webhook: WebhookConfig
    admin: AdminConfig
    rate_limit: RateLimitConfig
    redis: RedisConfig = RedisConfig()
    cache: CacheConfig


settings = Settings()  # type: ignore
