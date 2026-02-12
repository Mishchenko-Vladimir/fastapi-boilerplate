from fastapi import APIRouter, Request

from core.config import settings
from core.templates import templates


router = APIRouter(prefix=settings.view.verify_email)


@router.get(
    "/",
    name="verify_email",
    include_in_schema=False,
)
def verify_email(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="auth/verification.html",
        context={},
    )
