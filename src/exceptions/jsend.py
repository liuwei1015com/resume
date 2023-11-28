class JSendException(Exception):
    def __init__(self, status_code: int, message: str, data: dict = None):
        if not (400 <= status_code < 500):
            raise ValueError("JSendException status_code must be between 400 and 499")

        self.status_code = status_code
        self.message = message
        self.status = "fail"
        self.data = data
