import click
import os
import psycopg2
from flask import current_app, g
from flask.cli import with_appcontext
import os


def get_db():
    if 'db' not in g:

        g.db = psycopg2.connect(os.getenv("DATABASE_URL"))

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('postgres_schema.sql') as f:
        db.cursor().execute(f.read().decode('utf8'))
        db.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
