DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

GRAY = "\033[90m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

STATUS_CODE_COLORS = {
    "1": BLUE,
    "2": GREEN,
    "3": GRAY,
    "4": RED,
    "5": PURPLE,
}

LEVEL_COLORS = {
    "DEBUG": BLUE,
    "INFO": GREEN,
    "WARNING": YELLOW,
    "ERROR": RED,
    "CRITICAL": PURPLE,
}

METHOD_COLORS = {
    "GET": BLUE,
    "POST": GREEN,
    "PUT": YELLOW,
    "PATCH": YELLOW,
    "DELETE": RED,
}
