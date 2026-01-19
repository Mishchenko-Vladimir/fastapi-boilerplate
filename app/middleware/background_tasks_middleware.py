from fastapi import Request, Response
from fastapi.background import BackgroundTasks


async def background_tasks_middleware(request: Request, call_next):
    """
    Добавляет BackgroundTasks в request.state.background.
    Автоматически присоединяет задачи к ответу.
    """
    request.state.background = BackgroundTasks()
    response: Response = await call_next(request)

    if request.state.background.tasks:
        if response.background is None:
            response.background = request.state.background
        else:
            response.background.tasks.extend(request.state.background.tasks)  # type: ignore

    return response
