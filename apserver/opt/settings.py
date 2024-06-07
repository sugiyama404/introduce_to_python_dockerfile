import configparser
import os

work_dir = "/app/opt"

conf = configparser.ConfigParser()
conf.read(work_dir + '/settings.ini', encoding='utf-8')

time_zone = conf['DEFAULT']['TimeZone']
web_port = int(conf['web']['port'])

dbuser=os.getenv('DATABASE_USER')
dbpassword=os.getenv('DATABASE_PASSWORD')
dbhost=os.getenv('DATABASE_HOST')
dbname=os.getenv('DATABASE_NAME')
dbport=os.getenv('DATABASE_PORT')

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{dbuser}:{dbpassword}@{dbhost}/{dbname}?charset=utf8'

debug_mode = True if os.getenv('DEBUG_MODE', True) in ('true', True) else False

