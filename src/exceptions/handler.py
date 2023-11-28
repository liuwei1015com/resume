from fastapi.exceptions import RequestValidationError, StarletteHTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from shortuuid import ShortUUID

from src.configs import DEBUG_MODE
from src.utils.logger import ResponseLogContent, err_logger, logger, res_logger

from .jsend import JSendException


def jsend_handler(req: Request, exc: JSendException):
    content = {"status": exc.status, "message": exc.message}
    if DEBUG_MODE:
        content["detail"] = exc.data
    return JSONResponse(
        status_code=exc.status_code,
        content=content,
    )


def not_found_handler(req: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=404,
        content={"status": "fail", "message": "No Resource Found"},
    )


def validation_handler(req: Request, exc: RequestValidationError):
    err_id = ShortUUID().random(length=8)
    logger.error(f"[{err_id}]     Validation Error")
    err_logger.error(f"[{err_id}]     Validation Error\n{exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={"status": "fail", "message": "Validation Error", "data": exc.errors()},
    )


def server_error_handler(req: Request, exc: Exception):
    err_id = ShortUUID().random(length=8)
    logger.error(f"[{err_id}]     {exc}")
    err_logger.error(f"[{err_id}]     Internal Server Error", exc_info=exc)
    res_content = ResponseLogContent(
        path=req.url.path,
        method=req.method,
        ip_address=req.client.host,
        status_code=500,
    )
    res_logger.info(str(res_content.model_dump()))

    content = {"status": "error", "message": "Internal Server Error"}
    if DEBUG_MODE:
        content["detail"] = exc.__str__()
    return JSONResponse(status_code=500, content=content)
