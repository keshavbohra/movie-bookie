import os
import unittest
from main import create_app, db
from blueprints import blueprint
from main.model import movie, screening, theatre, user, booking, blacklist
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()
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