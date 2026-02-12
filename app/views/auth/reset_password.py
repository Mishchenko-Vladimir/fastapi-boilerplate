from fastapi import APIRouter, Request

from core.config import settings
from core.templates import templates


router = APIRouter(prefix=settings.view.password_reset)


@router.get(
    "/",
    name="password_reset",
    include_in_schema=False,
)
def password_reset(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="auth/reset-password.html",
        context={},
    )
