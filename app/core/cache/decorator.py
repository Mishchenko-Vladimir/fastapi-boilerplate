from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from core.config import settings


def conditional_cache(*cache_args, **cache_kwargs):
    """
    Условный декоратор кэширования: применяет кэширование только если оно включено в настройках.

    Обёртка над `@cache` из `fastapi-cache`, которая проверяет `settings.cache.enabled`.
    Если кэширование отключено — функция выполняется без кэширования.

    Args:
        *cache_args: Позиционные аргументы, передаваемые в `@cache` (например, время жизни).
        **cache_kwargs: Именованные аргументы, передаваемые в `@cache` (например, `namespace`, `key_builder`).

    Returns:
        Callable: Декоратор `@cache` (если кэш включён) или тождественная функция (если отключён).
    """
    if not settings.cache.enabled:
        # Если кэш отключён — возвращаем функцию без изменений
        return lambda func: func

    # Иначе — применяем настоящий @cache
    return cache(*cache_args, **cache_kwargs)


def conditional_clear(*args, **kwargs):
    """
     Условная очистка кэша: вызывает `FastAPICache.clear()` только если кэширование включено.

    Предотвращает попытки очистки кэша, когда он отключён (например, в тестах или dev-среде).
    Безопасно использовать в любом окружении.

    Args:
        *args: Позиционные аргументы для `FastAPICache.clear()` (например, `namespace`).
        **kwargs: Именованные аргументы для `FastAPICache.clear()` (например, `prefix`).

    Returns:
        Awaitable[None] | None: Результат `FastAPICache.clear()` (если кэш включён), иначе `None`.
    """
    if settings.cache.enabled:
        return FastAPICache.clear(*args, **kwargs)
    return None
