import pytest
from flask import Flask
from opt.main import user_bp
from opt.domain.user import User

@pytest.fixture
def app():
    """
    Flaskのテスト用アプリケーションをセットアップ
    """
    app = Flask(__name__)
    app.register_blueprint(user_bp)
    app.testing = True
    return app

@pytest.fixture
def client(app):
    """
    テスト用クライアントをセットアップ
    """
    return app.test_client()

def test_get_users(client):
    """
    get_usersの正常な動作をテストする
    """
    response = client.get('/user')
    assert response.status_code == 200

def test_get_users_no_users(client, mocker):
    """
    ユーザーがいない場合のget_usersをテストする
    """
    mocker.patch('opt.application.usecases.user_usecase.UserUsecase.get_all_users',return_value=None)
    response = client.get('/user')
    assert response.status_code == 404
    assert response.json == {'message': 'No users found'}

def test_get_user_success(client, mocker):
    """
    特定のIDのユーザーが存在する場合のget_userをテストする
    """
    user_id = 1
    mock_user = User(UserID=user_id, UserName="example_username", Email="example@example.com")

    mocker.patch('opt.application.usecases.user_usecase.UserUsecase.get_user_by_id', return_value=mock_user)
    response = client.get(f'/user/{user_id}')
    assert response.status_code == 200
    assert response.json == {'id': user_id, 'username': 'example_username', 'email': 'example@example.com'}

def test_get_user_not_found(client, mocker):
    """
    特定のIDのユーザーが存在しない場合のget_userをテストする
    """
    user_id = 1
    mocker.patch('opt.application.usecases.user_usecase.UserUsecase.get_user_by_id', side_effect=Exception("User not found"))

    response = client.get(f'/user/{user_id}')
    assert response.status_code == 404
    assert response.json == {'message': 'User not found'}

def test_create_user_success(client, mocker):
    """
    正常なユーザー作成のテスト
    """
    user_data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    }

    mock_user = User(UserID=1, UserName=user_data['username'], Email=user_data['email'])
    mocker.patch('opt.application.usecases.user_usecase.UserUsecase.create_user', return_value=mock_user)

    response = client.post('/user', json=user_data)
    assert response.status_code == 201
    assert response.json == {'id': '1', 'username': user_data['username'], 'email': user_data['email']}

def test_create_user_invalid_request(client, mocker):
    """
    不正なリクエストでユーザー作成が失敗する場合のテスト
    """
    invalid_user_data = {
        'username': 'testuser',
        # 'email' フィールドが欠如している
        'password': 'password123'
    }
    mocker.patch('opt.application.usecases.user_usecase.UserUsecase.create_user', side_effect=Exception("Invalid request"))

    response = client.post('/user', json=invalid_user_data)
    assert response.status_code == 400
    assert response.json == {'message': 'Invalid request'}

def test_update_user_success(client, mocker):
    """
    特定のIDのユーザーが正常に更新される場合のテスト
    """
    user_id = 1
    user_data = {
        'username': 'updateduser',
        'email': 'updateduser@example.com',
        'password': 'newpassword123'
    }

    mock_user = User(UserID=user_id, UserName=user_data['username'], Email=user_data['email'])

    # update_userメソッドをモックして、更新されたユーザーを返すようにする
    mocker.patch('opt.application.usecases.user_usecase.UserUsecase.update_user', return_value=mock_user)

    response = client.put(f'/user/{user_id}', json=user_data)
    assert response.status_code == 200
    assert response.json == {'id': user_id, 'username': user_data['username'], 'email': user_data['email']}

def test_update_user_not_found(client, mocker):
    """
    特定のIDのユーザーが存在しない場合のテスト
    """
    user_id = 1
    user_data = {
        'username': 'updateduser',
        'email': 'updateduser@example.com',
        'password': 'newpassword123'
    }

    # update_userメソッドをモックして、例外をスローするようにする
    mocker.patch('opt.application.usecases.user_usecase.UserUsecase.update_user', side_effect=Exception("User not found"))

    response = client.put(f'/user/{user_id}', json=user_data)
    assert response.status_code == 404
    assert response.json == {'message': 'User not found'}

def test_delete_user_success(client, mocker):
    """
    特定のIDのユーザーが正常に削除される場合のテスト
    """
    user_id = 1

    # delete_userメソッドをモックして、正常に動作するようにする
    mocker.patch('opt.application.usecases.user_usecase.UserUsecase.delete_user', return_value=None)

    response = client.delete(f'/user/{user_id}')
    assert response.status_code == 200
    assert response.json == {'message': 'User deleted successfully'}

def test_delete_user_not_found(client, mocker):
    """
    特定のIDのユーザーが存在しない場合のテスト
    """
    user_id = 1

    # delete_userメソッドをモックして、例外をスローするようにする
    mocker.patch('opt.application.usecases.user_usecase.UserUsecase.delete_user', side_effect=Exception("User not found"))

    response = client.delete(f'/user/{user_id}')
    assert response.status_code == 404
    assert response.json == {'message': 'User not found'}
