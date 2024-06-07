from flask import Blueprint, jsonify
from opt.application.usecases.user_usecase import UserUsecase
from opt.application.services.user_service import UserService
from opt.application.repositories.user_repository import UserRepository
from opt.domain.user import User

from opt.framework.database.models import get_engine
from flask import request
conn = get_engine()

user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['GET'])
def get_users():
    """
    すべてのユーザーを取得します。
    Returns:
        200:
            JSON形式のレスポンス: ユーザーの情報
        404:
            description: ユーザーが見つかりません
    """
    user_usecase = UserUsecase(UserService(UserRepository(conn)))
    users = user_usecase.get_all_users()
    if users is None:
        return jsonify({'message': 'No users found'}), 404
    else:
        return jsonify([{'id': user.UserID, 'username': user.UserName, 'email': user.Email} for user in users]), 200

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    特定のIDのユーザーを取得します。
    Returns:
        200:
            JSON形式のレスポンス: ユーザーの情報
        400:
            description: ユーザーが見つかりません
    """
    user_usecase = UserUsecase(UserService(UserRepository(conn)))
    try:
        user = user_usecase.get_user_by_id(user_id)
        return jsonify({'id': user.UserID, 'username': user.UserName, 'email': user.Email}), 200
    except Exception as e:
        return jsonify({'message': 'User not found'}), 404

@user_bp.route('/user', methods=['POST'])
def create_user():
    """
    新しいユーザーを作成します。
    responses:
        201:
            description: ユーザーの情報
        400:
            description: 要求が不正です
    """
    data = request.get_json()
    try:
        req_user = User(UserName=data['username'], Email=data['email'], Password=data['password'])
        user_usecase = UserUsecase(UserService(UserRepository(conn)))
        user = user_usecase.create_user(req_user)
        return jsonify({'id': str(user.UserID), 'username': user.UserName, 'email': user.Email}), 201
    except Exception as e:
        return jsonify({'message': 'Invalid request'}), 400

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    特定のIDのユーザーを更新します。
    responses:
        200:
            description: 更新されたユーザーの情報
        404:
            description: ユーザーが見つかりませんでした
    """
    user_usecase = UserUsecase(UserService(UserRepository(conn)))
    data = request.get_json()
    try:
        update_user = User(UserID=user_id, UserName=data['username'], Email=data['email'], Password=data['password'])
        user = user_usecase.update_user(update_user)
        return jsonify({'id': user.UserID, 'username': user.UserName, 'email': user.Email}), 200
    except Exception as e:
        return jsonify({'message': 'User not found'}), 404

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    特定のIDのユーザーを削除します。
    responses:
        200:
            description: ユーザーが削除されました
        404:
            description: ユーザーが見つかりませんでした
    """
    user_usecase = UserUsecase(UserService(UserRepository(conn)))
    try:
        user_usecase.delete_user(user_id)
        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'User not found'}), 404

