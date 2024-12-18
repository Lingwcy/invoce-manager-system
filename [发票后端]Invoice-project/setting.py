# 发票系统全局配置文件
class Config(object):
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = 'none'
    HOSTNAME = '127.0.0.1'
    DATABASE = 'sakila'
    PORT = 3306
    USERNAME = 'root'
    PASSWORD = '1633476211'
    DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True