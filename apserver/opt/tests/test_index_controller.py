import pytest
from flask import Flask
from opt.main import index_bp

@pytest.fixture
def app():
    """
    Flaskのテスト用アプリケーションをセットアップ
    """
    app = Flask(__name__)
    app.register_blueprint(index_bp)
    app.testing = True
    return app

@pytest.fixture
def client(app):
    """
    テスト用クライアントをセットアップ
    """
    return app.test_client()

def test_health_check(client):
    """
    ヘルスチェックエンドポイントのテスト
    """
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"answer": "helloworld"}
