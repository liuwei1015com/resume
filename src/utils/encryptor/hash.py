from bcrypt import checkpw, gensalt, hashpw


def hash_pwd(password: str) -> bytes:
    salt: str = gensalt(rounds=10)
    hashed: bytes = hashpw(password.encode("utf-8"), salt)
    return hashed


def verify_pwd(password: str, hashed: str):
    is_valid: bool = checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    return is_valid
