from uvicorn import run

from src.configs import ENV, HOST, PORT
from src.utils.logger import logger

APP_COMMAND: str = "src.main:app"
WILDCARD_HOST: str = "0.0.0.0"

if __name__ == "__main__":
    try:
        logger.info(f"Server is running at http://{HOST}:{PORT}")
        logger.info(f"Visit http://{HOST}:{PORT}/docs for the API documentation")

        match (ENV):
            case ("dev"):
                run(APP_COMMAND, host=WILDCARD_HOST, port=PORT, reload=True, access_log=False, log_level="critical")
            case ("prod"):
                run(APP_COMMAND, host=WILDCARD_HOST, port=PORT, reload=False, access_log=False, log_level="critical")
            case _:
                raise ValueError(f"Unknown environment: {ENV}")

    except Exception as exc:
        logger.exception(exc)
    finally:
        logger.warning("Server is stopped")
