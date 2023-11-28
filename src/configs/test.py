from decouple import config

KEEP_TEST_DATA: bool = config("KEEP_TEST_DATA", cast=bool)
