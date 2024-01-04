class PasswordInvalidError(Exception):

    def __str__(self):
        return self.message


class PasswordLengthError(PasswordInvalidError):
    message = 'Пароль должен быть не менее 8 символов'


class PasswordContainUpperError(PasswordInvalidError):
    message = 'Пароль должен содержать хотя бы одну заглавную букву'


class PasswordContainDigitError(PasswordInvalidError):
    message = 'Пароль должен содержать хотя бы одну цифру'


class User:

    def __init__(self, username, password=None):
        self.username = username
        if password is not None:
            self.set_password(password)

    def set_password(self, password):
        if len(password) < 8:
            raise PasswordLengthError
        if not any(i.isupper() for i in password):
            raise PasswordContainUpperError
        if not any(i.isdigit() for i in password):
            raise PasswordContainDigitError
        self.password = password


if __name__ == '__main__':
    assert issubclass(PasswordInvalidError, Exception)
    assert issubclass(PasswordLengthError, PasswordInvalidError)
    assert issubclass(PasswordContainUpperError, PasswordInvalidError)
    assert issubclass(PasswordContainDigitError, PasswordInvalidError)

    user = User("johndoe")

    try:
        user.set_password("weakpwd")
    except PasswordLengthError as e:
        print(e)

    try:
        user.set_password("strongpassword8")
    except PasswordContainUpperError as e:
        print(e)

    try:
        user.set_password("Safepassword")
    except PasswordContainDigitError as e:
        print(e)

    user.set_password("SecurePass123")
    assert user.password == 'SecurePass123'
