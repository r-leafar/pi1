from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask.sessions import NullSession
from werkzeug.security import check_password_hash, generate_password_hash
import os
import uuid
from minio import Minio
from minio.error import S3Error
from pi_turma4.db import get_db
import psycopg2.extras
from datetime import timedelta
import os

bp = Blueprint('naturalweb', __name__, url_prefix='/')

@bp.route('/')
def index():
    return os.environ.get("FLASK_APP")

@bp.route('/j2mhw82dyu1kn5g4')
def j2mhw82dyu1kn5g4():
    return os.environ.get("DATABASE_URL")