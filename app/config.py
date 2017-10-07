import os
from flask import current_app



_BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
        Default Config
    """
    DEBUG = False
    SECRET_KEY = os.urandom(24)


class Production(Config):
    """
        ProductionConfig
    """
    URL_PREFIX = ''


class Development(Config):
    """
        DevelopmentConfig
    """
    DEBUG = True
    URL_PREFIX = ''


class Testing(Config):
    """
        TestingConfig
    """
    TESTING = True


config = {
    'DEFAULT': Config,
    'PRODUCTION': Production,
    'DEVELOPMENT': Development,
    'TESTING': Testing
}


def get_config():
    """
        Return an application configuration
    """
    return current_app.config
