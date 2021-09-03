import os
import unittest

from .main import create_app, db
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'dev')
migrate = Migrate(app, db)

@app.cli.command()
def test():
    """
    Function to run unit testcases.
    """
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    results = unittest.TextTestRunner(verbosity=2).run(tests)
    
    if results.wasSuccessful():
        return 0
    
    return 1