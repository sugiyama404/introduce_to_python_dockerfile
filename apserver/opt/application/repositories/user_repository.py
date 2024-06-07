from opt.domain.user import User

from typing import List
from sqlalchemy.orm import Session

class UserRepository:
    """ユーザーリポジトリクラス。ユーザーデータのCRUD操作を提供します。"""
    def __init__(self, conn):
        """
        コンストラクタ。データベース接続を受け取ります。
        Args:
            conn: データベース接続オブジェクト
        """
        self.conn = conn

    def get_all_users(self) -> List[User]:
        """すべてのユーザーを取得します。
        Returns:
            List[User]: ユーザーリスト
        """
        session = Session(self.conn)
        users = session.query(User).all()
        return users

    def get_user_by_id(self, user_id: int) -> User:
        """
        指定されたIDのユーザーを取得します。
        Args:
            user_id: ユーザーID
        Returns:
            User: ユーザーオブジェクト
        """
        session = Session(self.conn)
        user = session.query(User).filter_by(UserID=user_id).first()
        if user is None:
            raise ValueError(f"User with ID {user_id} not found.")
        return user

    def create_user(self, user: User) -> User:
        """
        新しいユーザーを作成します。
        Args:
            user: 作成するユーザーオブジェクト
        Returns:
            User: 作成されたユーザーオブジェクト
        """
        session = Session(self.conn)
        session.add(user)
        session.commit()
        new_user = session.query(User)\
            .filter_by(Email=user.Email)\
            .order_by(User.UserID.desc())\
            .first()
        if new_user is None:
            raise RuntimeError("Failed to create user.")
        return new_user

    def update_user(self, user: User) -> User:
        """
        既存のユーザーを更新します。
        Args:
            user: 更新するユーザーオブジェクト
        Returns:
            User: 更新されたユーザーオブジェクト
        """
        session = Session(self.conn)
        session.merge(user)
        session.commit()
        new_user = session.query(User).filter_by(UserID=user.UserID).first()
        if new_user is None:
            raise RuntimeError("Failed to update user.")
        return new_user

    def delete_user(self, user_id: int) -> None:
        """指定されたIDのユーザーを削除します。
        Args:
            user_id: ユーザーID
        """
        session = Session(self.conn)
        user = session.query(User).filter_by(UserID=user_id).first()
        if user is None:
            raise ValueError(f"User with ID {user_id} not found.")
        session.delete(user)
        session.commit()
