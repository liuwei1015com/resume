from decouple import config

ENV: str = config("ENV")
HOST: str = config("HOST")
PORT: int = config("PORT", cast=int)
LANGUAGE: str = config("LANGUAGE")
DEBUG_MODE: bool = config("DEBUG_MODE", cast=bool, default=False)
SYSTEM_USERNAME: str = config("SYSTEM_USERNAME")
SYSTEM_PASSWORD: str = config("SYSTEM_PASSWORD")

if ENV.lower() in ["d", "dev", "develop", "development"]:
    ENV = "dev"
elif ENV.lower() in ["p", "prod", "product", "production"]:
    ENV = "prod"
else:
    raise ValueError("ENV is not valid")
