from fastapi import Request
from fastapi.responses import JSONResponse


class NotFoundException(Exception):

    def __init__(self, message: str):
        self.message = message


async def not_found_exception_handler(
    request: Request,
    exc: NotFoundException
):

    return JSONResponse(
        status_code=404,
        content={"error": exc.message}
    )