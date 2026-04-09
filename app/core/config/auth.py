from pydantic import BaseModel, SecretStr


class AccessToken(BaseModel):
    """Настройки токена"""

    # Срок жизни токена
    lifetime_seconds: int = 3600

    reset_password_token_secret: SecretStr
    verification_token_secret: SecretStr


class AdminConfig(BaseModel):
    """Конфигурация администратора"""

    # True - Публичная форма аутентификации для администратора
    # False - SQLAdmin форма аутентификации
    use_public_admin_auth: bool = False
    admin_panel_url: str = "/admin-panel"

    admin_email: str
    admin_password: SecretStr
    secret_key: SecretStr


class RateLimitConfig(BaseModel):
    """Конфигурация ограничения частоты запросов (rate limiting)"""

    enabled: bool = True
    default_limits: list[str] = ["40/minute"]
