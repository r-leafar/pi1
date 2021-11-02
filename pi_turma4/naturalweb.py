import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from pi_turma4.db import get_db

bp = Blueprint('naturalweb', __name__, url_prefix='/naturalweb')

@bp.route('/')
def index():
    return render_template("index.html");

@bp.route('/pontoturistico')
def pontoturistico():
    return render_template("ponto_turistico.html");

@bp.route('/pontohistorico')
def pontohistorico():
    return render_template("ponto_historico.html");

@bp.route('/imagempontohistorico')
def imagempontohistorico():
    return render_template("imagem_ponto_historico.html");

@bp.route('/cadastro')
def cadastro():
    return render_template("cadastro.html");
