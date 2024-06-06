from opt.domain.user import User
from opt.application.services.user_service import UserService

from typing import List

class UserUsecase:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_all_users(self) -> List[User]:
        return self.user_service.get_all_users()

    def get_user_by_id(self, user_id: int) -> User:
        return self.user_service.get_user_by_id(user_id)
