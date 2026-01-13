from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.routers import led, sensors

from app.handlers.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    internal_exception_handler
)

app = FastAPI(
    title="Arduino Control API",
    version="1.0.0"
)

# CORS - configuración abierta
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Handlers globales
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, internal_exception_handler)

# Endpoints
app.include_router(led.router)
app.include_router(sensors.router)
