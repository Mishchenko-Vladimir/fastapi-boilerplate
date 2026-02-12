from fastapi import APIRouter, Request

from core.config import settings
from core.templates import templates


router = APIRouter(prefix=settings.view.change_password)


@router.get(
    "/",
    name="change_password",
    include_in_schema=False,
)
def change_password(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="auth/forgot-password.html",
        context={},
    )
