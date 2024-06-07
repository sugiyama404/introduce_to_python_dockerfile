from sqlalchemy import create_engine

import settings

def get_engine()->any:
    """
    データベース接続URIを使ってSQLAlchemyエンジンオブジェクトを作成し、返します。
    Returns:
        Any: SQLAlchemy エンジンオブジェクト。
    """
    return create_engine(settings.SQLALCHEMY_DATABASE_URI)
