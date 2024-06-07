import pytest
from sqlalchemy.orm import sessionmaker

from opt.domain.user import User
from opt.application.services.user_service import UserService
from opt.application.repositories.user_repository import UserRepository

from opt.framework.database.models import get_engine

@pytest.fixture
def connection():
    conn = get_engine()
    yield conn

@pytest.fixture
def session(connection):
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()

@pytest.fixture
def user_service(connection):
    return UserService(UserRepository(connection))

def test_get_all_users(user_service, session):
    user1 = User(UserName= 'Alice', Email= 'example@example.com', Password="example")
    user2 = User(UserName= 'Bob', Email= 'example@example.com', Password="example")
    session.add(user1)
    session.add(user2)
    session.commit()

    # get_all_usersメソッドのテスト
    users = user_service.get_all_users()
    flag_alice = False
    flag_bob = False
    for u in users:
        if u.UserName == "Alice":
            flag_alice = True
        if u.UserName == "Bob":
            flag_bob = True

    if flag_alice & flag_alice:
        assert True
    else:
        assert False

def test_get_user_by_id_success(user_service, session):
    user1 = User(UserName= 'Alice', Email= 'example@example.com', Password="example")
    session.add(user1)
    session.commit()

    get_user = session.query(User).filter_by(UserName= 'Alice').first()

    # get_user_by_idメソッドのテスト
    user = user_service.get_user_by_id(get_user.UserID)
    assert user.UserName == "Alice"

def test_get_user_by_id_not_found(user_service, session):
    get_user = session.query(User).order_by(User.UserID.desc()).first()
    nf_id = get_user.UserID + 1
    with pytest.raises(ValueError, match=f"User with ID {nf_id} not found."):
        user_service.get_user_by_id(nf_id)


def test_create_user_success(user_service):
    # create_userメソッドのテスト
    user1 = User(UserName= 'Alice', Email= 'example@example.com', Password="example")
    user = user_service.create_user(user1)
    assert user.UserName == "Alice"

def test_update_user_success(user_service, session):
    user1 = User(UserName= 'Alice', Email= 'example@example.com', Password="example")
    session.add(user1)
    session.commit()

    # update_userメソッドのテスト
    user2 = User(UserID = 1, UserName= 'Bob', Email= 'example@example.com', Password="example")
    user = user_service.update_user(user2)
    assert user.UserName == "Bob"

def test_update_user_not_found(user_service, session):
    # 存在しないユーザーを更新しようとする
    get_user = session.query(User).order_by(User.UserID.desc()).first()
    nf_id = get_user.UserID + 1
    user = User(UserID=nf_id, UserName='NonExistent', Email='nonexistent@example.com', Password="password")
    with pytest.raises(Exception, match=r"ユーザーの削除に失敗しました。"):
        user_service.update_user(user)

def test_delete_user_success(user_service, session):
    user = User(UserName= 'Alice', Email= 'example@example.com', Password="example")
    session.add(user)
    session.commit()

    get_user = session.query(User).filter_by(UserName= 'Alice').first()
    user_service.delete_user(get_user.UserID)


def test_delete_user_not_found(user_service, session):
    # delete_userメソッドのテスト（異常系: ユーザーが存在しない場合）
    user = User(UserName= 'Alice', Email= 'example@example.com', Password="example")
    session.add(user)
    session.commit()

    get_user = session.query(User).filter_by(UserName= 'Alice').first()
    session.delete(get_user)
    session.commit()
    with pytest.raises(Exception, match=f"ユーザーの削除に失敗しました。"):
        user_service.delete_user(get_user.UserID)

