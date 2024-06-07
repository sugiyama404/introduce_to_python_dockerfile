from opt.domain.user import User
from opt.application.repositories.user_repository import UserRepository

from typing import List

class UserService:
    """
    ユーザーサービスクラス。ユーザーに関する操作を提供します。
    """
    def __init__(self, user_repository: UserRepository):
        """
        ユーザーサービスを初期化します。
        Args:
            user_repository (UserRepository): ユーザーリポジトリ
        """
        self.user_repository = user_repository

    def get_all_users(self) -> List[User]:
        """
        すべてのユーザーを取得します。
        Returns:
            List[User]: ユーザーリスト
        """
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id: int) -> User:
        """
        指定されたIDのユーザーを取得します。
        Args:
            user_id (int): ユーザーID
        Returns:
            User: ユーザーオブジェクト
        Raises:
            ValueError: ユーザーが見つからない場合
        """
        user = self.user_repository.get_user_by_id(user_id)
        if user is None:
            raise ValueError(f"User with ID {user_id} not found.")
        return user

    def create_user(self, user: User) -> User:
        """
        新しいユーザーを作成します。
        Args:
            user (User): 作成するユーザー情報
        Returns:
            User: 作成されたユーザー情報
        Raises:
            Exception: ユーザーの作成に失敗した場合
        """
        try:
            return self.user_repository.create_user(user)
        except Exception as e:
            raise Exception("ユーザーの作成に失敗しました。") from e

    def update_user(self, user: User) -> User:
        """
        既存のユーザー情報を更新します。
        Args:
            user (User): 更新するユーザー情報
        Returns:
            User: 更新されたユーザー情報。ユーザーが存在しない場合はNone
        Raises:
            Exception: ユーザーの更新に失敗した場合
        """
        try:
            return self.user_repository.update_user(user)
        except Exception as e:
            raise Exception("ユーザーの削除に失敗しました。") from e

    def delete_user(self, user_id: int) -> None:
        """
        ユーザーを削除します。
        Args:
            user_id (int): 削除するユーザーのID
        Raises:
            Exception: ユーザーの削除に失敗した場合
        """
        try:
            self.user_repository.delete_user(user_id)
        except Exception as e:
            raise Exception("ユーザーの削除に失敗しました。") from e
