from os import getcwd, makedirs
from os.path import exists, join

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.exceptions import JSendException, RequestValidationError, jsend_handler, not_found_handler
from src.exceptions import server_error_handler, validation_handler
from src.middlewares import response_handler
from src.routes import main_router

app = FastAPI(
    title="ZDX905 API Documentation",
    version="0.1.0",
)

app.include_router(main_router)

app.middleware("http")(response_handler)

app.add_exception_handler(JSendException, jsend_handler)
app.add_exception_handler(RequestValidationError, validation_handler)
app.add_exception_handler(404, not_found_handler)
app.add_exception_handler(Exception, server_error_handler)

ROOT_DIR: str = getcwd()
PUBLIC_DIR: str = join(ROOT_DIR, "public")

if not exists(PUBLIC_DIR):
    makedirs(PUBLIC_DIR)

app.mount("/", StaticFiles(directory="public", html="index.html"), name="public")
