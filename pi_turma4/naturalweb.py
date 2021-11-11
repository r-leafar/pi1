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

@bp.route('/teste')
def teste():
    cur = get_db().execute("select * from usuario")
    rs = cur.fetchall()
    cur.close()

    from werkzeug.security import generate_password_hash, check_password_hash
  
    print (rs[0]["nome"])
    print (check_password_hash(rs[0][2],'1234'))

    #print(generate_password_hash('123',method='pbkdf2:sha256'));

    return "dxdsd"


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
     from werkzeug.security import generate_password_hash, check_password_hash
    
     if request.method == 'GET':
        return render_template("login.html");
     else:

        cur = get_db().execute("SELECT senha FROM usuario WHERE nome LIKE ?",[request.form['user']])
        rs = cur.fetchone()
    
        if check_password_hash(rs[0], request.form['password']):
                     
                     session["user"] = request.form['user']
                     return render_template("index.html");
        else:
            flash('Você digitou o usuário e/ou senha inválido')
            return redirect(url_for("naturalweb.login"));

@bp.route('/cadastrousuario')
def cadastrousuario():
    cur = get_db().execute("select * from usuario")
    rs = cur.fetchall()
    cur.close()

    return render_template("cadastro_usuario.html",usuarios=rs);

@bp.route('/editarusuario/<int:idusuario>',methods = ['GET','POST'])
def editarusuario(idusuario):
    if request.method == 'GET':
        cur = get_db().execute("select * from usuario where idusuario=%s"%idusuario)
        usuario = cur.fetchone()
        cur.close()
        return  render_template("edita_usuario.html",usuario=usuario);
    else:
        from werkzeug.security import generate_password_hash
        if request.form['password']==request.form['password_confirm']:
            cur = get_db().execute("UPDATE usuario set senha=? WHERE idusuario=?",[generate_password_hash(request.form['password']),idusuario])
            cur.close()
            get_db().commit()
            return "atualizado confere"
        else:
            return "Não confere"

@bp.route('/cadastroponto')
def cadastroponto():
    return render_template("cadastro_ponto.html");

@bp.route('/logout')
def logout():
    session.clear()
    return render_template("index.html");
