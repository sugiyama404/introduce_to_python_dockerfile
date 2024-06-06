from sqlalchemy import create_engine

import settings

def get_engine():
    return create_engine(settings.SQLALCHEMY_DATABASE_URI)
