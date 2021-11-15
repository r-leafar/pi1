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
from datetime import timedelta

bp = Blueprint('naturalweb', __name__, url_prefix='/')


def client_minio():
    return  Minio(
        "192.168.0.50:9000",
        access_key="univesp",
        secret_key="kk]9pT$[C.T9NX}?",
        secure=False
    )

@bp.route('/')
def index():
    return render_template("index.html");

def get_lista_usuario():
    cur = get_db().execute("select * from usuario")
    rs = cur.fetchall()
    cur.close()
    return rs

def get_ponto(idponto):
    sql = "select idponto,titulo,descricao,nomeimg,tipoponto from ponto WHERE idponto = ?"
    cur = get_db().execute(sql,[idponto])
    rs = cur.fetchall()
    cur.close()
    ponto= [dict(row) for row in rs]

    return ponto[0]

def get_lista_ponto(tipoponto=None):
    
    if tipoponto is None:
        sql = "select idponto,titulo,descricao,nomeimg,tipoponto from ponto"
        cur = get_db().execute(sql)
        rs = cur.fetchall()
        cur.close()
    else:
        sql = "select * from ponto where tipoponto=?"
        cur = get_db().execute(sql,[tipoponto])
        rs = cur.fetchall()
        cur.close()
    return rs

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

@bp.route('/cadastrousuario',methods = ['POST', 'GET'])
def cadastrousuario():
    
    if request.method == 'GET':
        rs = get_lista_usuario()
        return render_template("cadastro_usuario.html",usuarios=rs);
    else:
        # Validação se o usuario e senha estão corretos
        if request.form['password']==request.form['password_confirm']:
            from werkzeug.security import generate_password_hash

            cur = get_db().execute("INSERT INTO usuario (nome,senha,usuariocadastro) values(?,?,?)",[request.form['user'],generate_password_hash(request.form['password']),session["user"]])
            get_db().commit()

            rs = get_lista_usuario()
            flash('Usuario cadastrado com sucesso.')

            return render_template("cadastro_usuario.html",usuarios=rs);
        else:
            rs = get_lista_usuario()
            flash('Senhas estão diferentes, por favor, verifique.')
            return render_template("cadastro_usuario.html",usuarios=rs);
    

@bp.route('/editarusuario/<int:idusuario>',methods = ['GET','POST'])
def editarusuario(idusuario):
    if request.method == 'GET':
        cur = get_db().execute("select * from usuario where idusuario=?",[idusuario])
        usuario = cur.fetchone()
        cur.close()
        return  render_template("edita_usuario.html",usuario=usuario);
    else:
        from werkzeug.security import generate_password_hash
        from datetime import datetime, timezone

        if request.form['password']==request.form['password_confirm']:
            cur = get_db().execute("UPDATE usuario set senha=?,usuarioalteracao=?,alteradoem=? WHERE idusuario=?",[generate_password_hash(request.form['password']),session["user"],datetime.now().strftime("%Y-%m-%d %H:%M:%S"),idusuario])
            cur.close()
            get_db().commit()
            flash('Dados do usuário alterado com sucesso.')
            return render_template("cadastro_usuario.html", usuarios=get_lista_usuario())
        else:
            return "Não confere"

@bp.route('/cadastroponto',methods = ['GET','POST'])
def cadastroponto():
    
    if request.method == 'GET':
        return render_template("cadastro_ponto.html");
    else:
        if request.files["nomeimg"]:
            uploaded_file=request.files["nomeimg"]
            client = client_minio()
            size = os.fstat(uploaded_file.fileno()).st_size
            
            try:
                imgname = str(uuid.uuid4())
                imgname = imgname+"."+uploaded_file.filename.split(".")[1]
                
                cur = get_db().execute("INSERT INTO ponto (titulo,descricao,tipoponto,nomeimg,usuariocadastro) values(?,?,?,?,?)",[request.form['nomeponto'],request.form['descricao'],request.form['tipo'],imgname,session["user"]])
                get_db().commit()
                
                client.put_object("univesp",imgname,uploaded_file,size)

                flash("Ponto cadastrado com sucesso.")

                return render_template("cadastro_ponto.html");
            except S3Error as exc:
                 print("error occurred.", exc)

           

        '''
        rs = request.files["nomeimg"].mimetype+"</br></br>"
        rs += str(os.fstat(request.files["nomeimg"].fileno()).st_size)+"</br></br>"
        rs += str(request.files["nomeimg"].mimetype_params)+"</br></br>"
        rs += str(request.files["nomeimg"].content_type)+"</br></br>"
        rs +=request.form['nomeponto']+"</br></br>"
        rs +=request.form['tipo']+"</br></br>"
        rs +=request.form['descricao']+"</br></br>"'''
@bp.route('/editarponto/<int:idponto>',methods = ['GET','POST'])
def editaponto(idponto):
    if request.method == 'GET':
        
        ponto = get_ponto(idponto)
        print(ponto)
        return render_template("edita_ponto.html",ponto=ponto);
    else:
        pass

@bp.route('/listarponto/',methods = ['GET','POST'])
def listarponto():
    pontos= [dict(row) for row in get_lista_ponto()]
    client = client_minio()
    
    for p in pontos:
        p["nomeimg"] = client.get_presigned_url("GET","univesp",p["nomeimg"],expires=timedelta(days=1),)

    
    return render_template("listar_ponto.html",pontos=pontos)

     

@bp.route('/logout')
def logout():
    session.clear()
    return render_template("index.html");
