from opt.domain.user import User
from opt.application.repositories.user_repository import UserRepository

from typing import List

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self) -> List[User]:
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id: int) -> User:
        return self.user_repository.get_user_by_id(user_id)
