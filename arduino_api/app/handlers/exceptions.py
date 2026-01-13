from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

logger = logging.getLogger("arduino_api")

async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    # Maneja errores HTTP (404, 405, etc.)
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "path": request.url.path
        }
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Maneja errores de validación (422)
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation error",
            "details": exc.errors()
        }
    )

async def internal_exception_handler(request: Request, exc: Exception):
    # Maneja errores 500 no controlados
    logger.exception("Unhandled exception")

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error"
        }
    )
