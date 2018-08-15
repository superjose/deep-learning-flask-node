import os
from flask import Flask
import db.db as db
import db.auth as auth
import flaskr.json as json

def create_app(test_config = None):
    # Create and Configure the app
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent = True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # A simple Hello Bearsh
    @app.route('/')
    def hello():
        return "Caaaa Hello World from Flask 😁"

    # Connects the databse into the application
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(json.bp)
    return app
# END

# # # Original file:
# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Caaaa Hello World from Flask 8 🔥🔥🔥🔥🔥!! 😊"

# if __name__ == "__main__":
    # Only for debugging while developing
    # create_app().run(host='0.0.0.0', debug = True, port = 80)