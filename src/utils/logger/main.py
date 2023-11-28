from logging import DEBUG, INFO, Formatter, LogRecord, StreamHandler, getLogger
from logging.handlers import TimedRotatingFileHandler

from src.configs import DEBUG_MODE

from .settings import DATETIME_FORMAT, GRAY, LEVEL_COLORS, RESET


class MainFormatter(Formatter):
    def __init__(self, colored: bool = False):
        super().__init__()
        self.colored = colored

    def format(self, record: LogRecord) -> str:
        asctime: str = self.formatTime(record, DATETIME_FORMAT)
        levelname: str = record.levelname
        message: str = record.getMessage()

        level_color: str = LEVEL_COLORS.get(levelname, GRAY)

        colored_asctime = f"{GRAY}[{asctime}]{RESET}"
        colored_levelname = f"{level_color}{levelname:8s}{RESET}"

        if record.exc_info:
            exc_info = self.formatException(record.exc_info)
            formatted_exc_info = f"\n{exc_info}\n"
            message += formatted_exc_info

        if self.colored:
            return f"{colored_asctime} {colored_levelname} {message}"

        return f"[{asctime}] {levelname:8s} {message}"


logger = getLogger("main")
logger.setLevel(DEBUG if DEBUG_MODE else INFO)

stream_handler = StreamHandler()
stream_handler.setFormatter(MainFormatter(colored=True))

file_handler = TimedRotatingFileHandler(filename="log/main.log", when="midnight", backupCount=30, encoding="utf-8")
file_handler.setFormatter(MainFormatter())

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
