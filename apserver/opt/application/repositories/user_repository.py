from opt.domain.user import User

from typing import List
from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self, conn):
        self.conn = conn

    def get_all_users(self) -> List[User]:
        session = Session(self.conn)
        users = session.query(User).all()
        return users

    def get_user_by_id(self, user_id: int) -> User:
        session = Session(self.conn)
        user = session.query(User).filter_by(UserID=user_id).first()
        return user
