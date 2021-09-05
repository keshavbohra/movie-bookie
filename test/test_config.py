import os
import unittest

from flask import current_app
from flask_testing import TestCase

from app import app
from main.config import base_dir

class TestDevelopmentConfig(TestCase):
    
    def create_app(self):
        app.config.from_object('main.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'movie_secret_key')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(base_dir, 'dev_main.db'))


class TestTestingConfig(TestCase):
    
    def create_app(self):
        app.config.from_object('main.config.TestingConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'movie_secret_key')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(base_dir, 'test_main.db'))


class TestProductionConfig(TestCase):
    
    def create_app(self):
        app.config.from_object('main.config.ProductionConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'movie_secret_key')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(base_dir, 'prod_main.db'))
    

if __name__ == '__main__':
    unittest.main()