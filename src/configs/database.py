from decouple import config

DB_URI: str = config("DB_URI")
DB_DRIVER: str = config("DB_DRIVER")
DB_SERVER: str = config("DB_SERVER")
DB_PORT: int = config("DB_PORT", cast=int)
DB_DATABASE: str = config("DB_DATABASE")
DB_USER: str = config("DB_USER")
DB_PASSWORD: str = config("DB_PASSWORD")
