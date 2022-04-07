import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if user:
            raise UserInputError("Username already exists")

        if not re.match("^[a-z]{3,}$", username):
            raise UserInputError("Username is too short")

        if not re.match("^[a-z0-9]{8,}$", password):
            raise UserInputError("Password is too short")

        if not re.search("[0-9]+", password):
            raise UserInputError("Password should contain numbers")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
