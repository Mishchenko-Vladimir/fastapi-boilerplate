# Обработчик ошибок
import logging

from fastapi import FastAPI, Request, status

from pydantic import ValidationError
from sqlalchemy.exc import DatabaseError
from starlette.responses import RedirectResponse, JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

log = logging.getLogger(__name__)


def register_errors_handlers(app: FastAPI) -> None:
    """
    Регистрирует глобальные обработчики ошибок для приложения FastAPI.

    Args:
        app: Экземпляр FastAPI, в который добавляются обработчики.

    Добавляет обработчики для:
        - ValidationError (Pydantic)
        - DatabaseError (SQLAlchemy)
        - HTTPException (FastAPI)
        - Логирует критические ошибки
        - Перенаправляет пользователей при ошибках в UI

    Returns:
        - API-ошибки возвращают JSON
        - UI-ошибки (не API) перенаправляют на страницы (/page-missing)
    """

    @app.exception_handler(ValidationError)
    def handle_pydantic_validation_error(
        request: Request,
        exc: ValidationError,
    ) -> JSONResponse:
        """
        Обрабатывает ошибки валидации Pydantic при создании/обновлении моделей.

        :param request: Объект запроса (для логирования и анализа контекста).
        :param exc: Исключение ValidationError от Pydantic.
        :return: JSON-ответ, с деталями ошибок валидации и со статусом 422 Unprocessable Entity.
        """

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "message": "Ошибка валидации данных",
                "error": exc.errors(),
            },
        )

    @app.exception_handler(DatabaseError)
    def handle_db_error(
        request: Request,
        exc: DatabaseError,
    ) -> JSONResponse:
        """
        Обрабатывает критические ошибки базы данных (например, разрыв соединения).

        :param request: Объект запроса.
        :param exc: Исключение от SQLAlchemy (IntegrityError, OperationalError и др.).
        :return: JSON-ответ, с общим сообщением об ошибке и со статусом 500 Internal Server Error.
        """

        log.error(
            "Произошла ошибка базы данных",
            exc_info=exc,
        )
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "Произошла непредвиденная ошибка. "
                "Администраторы уже работают над решением."
            },
        )

    @app.exception_handler(StarletteHTTPException)
    def http_exception_handler(
        request: Request,
        exc: StarletteHTTPException,
    ):
        """
        Централизованный обработчик HTTP-исключений.

        Example:
            - Защита от раскрытия внутренних путей
            - Единое поведение для UI

        Args:
            request: Объект запроса.
            exc: HTTPException с кодом и деталями.

        Returns:
             - Для API-запросов: JSON с `{"detail": ...}`.
             - Для UI-запросов: редирект на /page-missing.
        """
        if request.url.path.startswith("/api"):
            return JSONResponse(
                status_code=exc.status_code,
                content={"detail": exc.detail},
            )

        if exc.status_code == 404:
            return RedirectResponse(url="/page-missing")
        if exc.status_code in (401, 403):
            return RedirectResponse(url="/page-missing")

        return RedirectResponse(url="/page-missing")
