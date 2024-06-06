from flask import Blueprint, jsonify


index_bp = Blueprint('index', __name__)

@index_bp.route('/', methods=['GET'])
def heltch_check():
    return jsonify([{"answer": "helloworld"}])
