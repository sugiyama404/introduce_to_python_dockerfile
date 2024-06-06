from flask import Blueprint, jsonify
from opt.application.usecases.user_usecase import UserUsecase
from opt.application.services.user_service import UserService
from opt.application.repositories.user_repository import UserRepository

from opt.framework.database.models import get_engine
conn = get_engine()

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
    user_usecase = UserUsecase(UserService(UserRepository(conn)))
    users = user_usecase.get_all_users()
    return jsonify([{'id': user.UserID, 'username': user.UserName, 'email': user.Email} for user in users])

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user_usecase = UserUsecase(UserService(UserRepository(conn)))
    user = user_usecase.get_user_by_id(user_id)
    return jsonify({'id': user.UserID, 'username': user.UserName, 'email': user.Email})
