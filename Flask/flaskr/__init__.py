import os

from flask import Flask

def create_app(test_config = None):
    # Create and configure the App
    app = Flask(__name__, instance_relative_config = True)

