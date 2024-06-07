from flask import Blueprint, jsonify


index_bp = Blueprint('index', __name__)

@index_bp.route('/', methods=['GET'])
def heltch_check():
    """
    ヘルスチェックエンドポイント
    Returns:
        JSON形式のレスポンス: {"answer": "helloworld"}
        ステータスコード: 200
    """
    return jsonify([{"answer": "helloworld"}]), 200
