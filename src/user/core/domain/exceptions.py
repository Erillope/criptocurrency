class UserAccountException(Exception):
    def __init__(self, message: str, code: int, *args: object) -> None:
        super().__init__(*args)
        self.message = message
        self.code = code
    
    @classmethod
    def without_password(cls, username: str) -> "UserAccountException":
        return cls(f"El usuario '{username}' no cuenta con una contraseña", 1)

    @classmethod
    def invalid_name(cls, name: str) -> "UserAccountException":
        return cls(f"El nombre proporcionado '{name}' no es válido", 2)
    
    @classmethod
    def invalid_username(cls, username: str) -> "UserAccountException":
        return cls(f"El nombre de usuario proporcionado '{username}' no es válido", 3)

    @classmethod
    def invalid_email(cls, email: str) -> "UserAccountException":
        return cls(f"El correo electrónico proporcionado '{email}' no es válido", 4)

    @classmethod
    def invalid_photo(cls, photo: str) -> "UserAccountException":
        return cls(f"La URL de la foto proporcionada '{photo}' no es válida", 5)

    @classmethod
    def invalid_password(cls) -> "UserAccountException":
        return cls("La contraseña proporcionada no es válida", 6)