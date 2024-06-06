import os

dbuser=os.getenv('DATABASE_USER')
dbpassword=os.getenv('DATABASE_PASSWORD')
dbhost=os.getenv('DATABASE_HOST')
dbname=os.getenv('DATABASE_NAME')
dbport=os.getenv('DATABASE_PORT')

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{dbuser}:{dbpassword}@{dbhost}/{dbname}?charset=utf8'

debug_mode = os.getenv('DEBUG_MODE')
if debug_mode == 'true':
    DEBUG = True
