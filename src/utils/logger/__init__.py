from os import getcwd, makedirs
from os.path import exists, join

ROOT_DIR: str = getcwd()
LOG_DIR: str = join(ROOT_DIR, "log")

if not exists(LOG_DIR):
    makedirs(LOG_DIR)

from .error import err_logger
from .main import logger
from .response import ResponseLogContent, res_logger
