import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask.sessions import NullSession
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

@bp.route('/login',methods = ['POST', 'GET'])
def login():
     if request.method == 'GET':
        return render_template("login.html");
     else:
         if request.form['user'] == 'admin' and request.form['password']=='123':
                     session["user"] = request.form['user']
                     return render_template("index.html");
         else:
             flash('Você digitou o usuário e/ou senha inválido')
             return redirect(url_for("naturalweb.login"));

@bp.route('/cadastrousuario')
def cadastrousuario():
    return render_template("cadastro_usuario.html");

@bp.route('/cadastroponto')
def cadastroponto():
    return render_template("cadastro_ponto.html");

@bp.route('/logout')
def logout():
    session.clear()
    return render_template("index.html");
