from slowapi import Limiter
from slowapi.util import get_remote_address

from core.config import settings


# Защита от спама (bruteforce).
if settings.rate_limit.enabled or settings.site.environment == "production":
    limiter = Limiter(
        key_func=get_remote_address,
        default_limits=settings.rate_limit.default_limits,
        enabled=True,
    )
else:
    limiter = Limiter(
        key_func=get_remote_address,
        default_limits=[],
        enabled=False,
    )
