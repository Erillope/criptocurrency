import hashlib

class PasswordChecker:
    def check(self, hashed_password: str, password: str) -> bool:
        return hashed_password == hashlib.sha256(password.encode()).hexdigest()

class PasswordHasher:
    def hash(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()