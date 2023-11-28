from logging import INFO, Formatter, LogRecord, StreamHandler, getLogger
from logging.handlers import TimedRotatingFileHandler

from pydantic import BaseModel

from .settings import DATETIME_FORMAT, GRAY, METHOD_COLORS, RESET, STATUS_CODE_COLORS


class ResponseLogContent(BaseModel):
    path: str
    method: str
    ip_address: str
    status_code: int


class ResponseFormatter(Formatter):
    def __init__(self, colored: bool = False):
        super().__init__()
        self.colored = colored

    def format(self, record: LogRecord) -> str:
        asctime: str = self.formatTime(record, DATETIME_FORMAT)
        message = ResponseLogContent.model_validate(eval(record.getMessage()))

        path = message.path
        method = message.method
        ip_address = message.ip_address
        status_code = message.status_code

        method_color: str = METHOD_COLORS.get(method, GRAY)
        status_code_color: str = STATUS_CODE_COLORS.get(str(status_code)[0], GRAY)

        colored_asctime = f"{GRAY}[{asctime}]{RESET}"
        colored_method = f"{method_color}[{method}]{RESET}"
        colored_ip_address = f"{GRAY}{ip_address:15s}{RESET}"
        colored_status_code = f"{status_code_color}{status_code}{RESET}"

        if self.colored:
            return f"{colored_asctime} {colored_ip_address} {colored_status_code} {colored_method} {path}"

        return f"[{asctime}] {ip_address:15s} {status_code} [{method}] {path}"


res_logger = getLogger("response")
res_logger.setLevel(INFO)

stream_handler = StreamHandler()
stream_handler.setFormatter(ResponseFormatter(colored=True))

file_handler = TimedRotatingFileHandler(filename="log/response.log", when="midnight", backupCount=14, encoding="utf-8")
file_handler.setFormatter(ResponseFormatter())

res_logger.addHandler(stream_handler)
res_logger.addHandler(file_handler)
