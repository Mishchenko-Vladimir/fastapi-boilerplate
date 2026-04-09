from pydantic import BaseModel


class ViewPrefix(BaseModel):
    """Конфигурация префикса для страниц"""

    home: str = ""
    page_missing: str = "/page-missing"
    limit_exceeded: str = "/limit-exceeded"
    verify_email: str = "/verify-email"
    change_password: str = "/change-password"
    password_reset: str = "/password-reset"
