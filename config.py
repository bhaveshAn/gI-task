# -*- coding: utf-8 -*-
import os

from envparse import env

env.read_envfile()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    The base configuration option. Contains the defaults.
    """

    DEBUG = False

    DEVELOPMENT = False
    STAGING = False
    PRODUCTION = False
    TESTING = False
    ETAG = True
    CSRF_ENABLED = True
    SERVER_URL = env('SERVER_URL', default=None)
    SQLALCHEMY_DATABASE_URI = env('DATABASE_URL', default=None)
    DATABASE_QUERY_TIMEOUT = 0.1
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API configs

    if not SQLALCHEMY_DATABASE_URI:
        print('`DATABASE_URL` either not exported or empty')
        exit()

    BASE_DIR = basedir
    FORCE_SSL = os.getenv('FORCE_SSL', 'no') == 'yes'

    if FORCE_SSL:
        PREFERRED_URL_SCHEME = 'https'


class ProductionConfig(Config):
    """
    The configuration for a production environment
    """

    MINIFY_PAGE = True
    PRODUCTION = True
    CACHING = True


class StagingConfig(ProductionConfig):
    """
    The configuration for a staging environment
    """

    PRODUCTION = False
    STAGING = True


class DevelopmentConfig(Config):
    """
    The configuration for a development environment
    """

    DEVELOPMENT = True
    DEBUG = True
    CACHING = True
    PROPOGATE_ERROR = True

    # Test database performance
    SQLALCHEMY_RECORD_QUERIES = True


class TestingConfig(Config):
    """
    The configuration for a test suit
    """
    TESTING = True
    SQLALCHEMY_RECORD_QUERIES = True
    SERVER_URL = env('TEST_SERVER_URL', default=None)
    SQLALCHEMY_DATABASE_URI = env('TEST_DATABASE_URL', default=None)
