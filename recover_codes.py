import secrets
from argon2 import PasswordHasher

ph = PasswordHasher()


def generate_recovery_codes(count=10):
    codes = []

    for _ in range(count):
        code = str(secrets.randbelow(100000000)).zfill(8)
        codes.append(code)

    return codes


def hash_recovery_code(code):
    return ph.hash(code)


def verify_recovery_code(code, code_hash):
    try:
        return ph.verify(code_hash, code)
    except Exception:
        return False