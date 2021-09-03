import os

base_dir = os.path.abspath(os.path.dirname(__name__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'movie_booking_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'dev_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'test_main.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'prod_main.db')

config_by_name = dict()

config_by_name['dev'] = DevelopmentConfig
config_by_name['test'] = TestingConfig
config_by_name['prod'] = ProductionConfig

key = Config.SECRET_KEY