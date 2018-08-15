# Testing out json with Flask!

from flask import (
    Blueprint, g, jsonify
)

bp = Blueprint('json', __name__, url_prefix = '/api')

@bp.route('/', methods = ('GET', 'POST'))
def index():
    return jsonify('Hello :D')