# config file

import os

SECRET_KEY = "Mysecret"


class Config(object):
    """Base config class"""
    DEBUG = False
    CSRF_ENABLED = True


class DevConfig(Config):
    """Configuration for development"""
    DEBUG = True


class TestConfig(Config):
    """Test config"""
    TESTING = True
    DEBUG = True
    CSRF_ENABLED = False


class StagingConfig(Config):
    """Staging configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Staging for production"""
    DEBUG = False
    TESTING = False
    DATABASE_URL: postgres: // cmcfpalbxxkgpo: 92a26a779471689f49b39abefd444ca966e1e5ad6ae0bca99ffaf635c24cbea1@ec2 - 23 - 23 - 130 - 158.compute - 1.amazonaws.com: 5432 / deqp08uur6q2gh


app_config = {
    'development': DevConfig,
    'testing': TestConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
