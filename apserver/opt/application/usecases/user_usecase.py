from opt.domain.user import User
from opt.application.services.user_service import UserService
from opt.utils.helper import generate_password_hash

from typing import List

class UserUsecase:
    """ユーザーユースケースクラス。ユーザー関連のビジネスロジックを提供します。"""
    def __init__(self, user_service: UserService):
        """コンストラクタ。ユーザーサービスを受け取ります。
        Args:
            user_service: ユーザーサービスオブジェクト
        """
        self.user_service = user_service

    def get_all_users(self) -> List[User]:
        """
        すべてのユーザーを取得します。
        Returns:
            List[User]: ユーザーリスト
        """
        return self.user_service.get_all_users()

    def get_user_by_id(self, user_id: int) -> User:
        """
        指定されたIDのユーザーを取得します。
        Args:
            user_id: ユーザーID
        Returns:
            User: ユーザーオブジェクト
        """
        try:
            return self.user_service.get_user_by_id(user_id)
        except Exception as e:
            raise Exception(f"Error getting user by ID {user_id}") from e

    def create_user(self, user: User) -> User:
        """
        新しいユーザーを作成します。
        Args:
            user: 作成するユーザーオブジェクト
        Returns:
            User: 作成されたユーザーオブジェクト
        """
        try:
            user.Password = generate_password_hash(user.Password)
            return self.user_service.create_user(user)
        except Exception as e:
            raise Exception(f"Error creating user") from e

    def update_user(self, user: User) -> User:
        """既存のユーザーを更新します。
        Args:
            user: 更新するユーザーオブジェクト
        Returns:
            User: 更新されたユーザーオブジェクト
        """
        try:
            user.Password = generate_password_hash(user.Password)
            return self.user_service.update_user(user)
        except Exception as e:
            raise Exception(f"Error updating user") from e

    def delete_user(self, user_id: int) -> None:
        """
        指定されたIDのユーザーを削除します。
        Args:
            user_id: ユーザーID
        """
        try:
            self.user_service.delete_user(user_id)
        except Exception as e:
            raise Exception(f"Error deleting user with ID {user_id}") from e
