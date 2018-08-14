import sqlite3

import click

from flask import current_app, g
from flask.cli import with_appcontext


# Registers the applicaiton through DI
def init_app(app):
    print('Got here!!')
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


def init_db_command():
    # Clear the existing data and create new tables
    init_db()
    click.echo('Database was initialized')


def get_db():
    # Reduces complexity
    if 'db' in g:
        return g.db

    g.db = sqlite3.connect(
        current_app.config['DATABASE'],
        detect_types = sqlite3.PARSE_DECLTYPES
    )
    g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e = None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

