import os


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


class DevelopmentConifg(BaseConfig):
    SECRET_KEY = 'LOCAL_SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'


class ProductionConfig(BaseConfig):
    DEBUG = False


config = {
    "development":DevelopmentConifg,
    "production":ProductionConfig
}