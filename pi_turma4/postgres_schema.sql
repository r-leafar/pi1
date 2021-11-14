DROP TABLE IF EXISTS ponto;

CREATE TABLE ponto (
  idponto serial PRIMARY KEY,
  titulo varchar(255) NOT NULL,
  descricao TEXT NOT NULL,
  nomeimg varchar(255) NOT NULL,
  criadoem date not null default CURRENT_DATE,
  alteradoem date not null default CURRENT_DATE,
  usuariocadastro varchar(255) NOT NULL,
  usuarioalteracao varchar(255)
);

DROP TABLE IF EXISTS usuario;

CREATE TABLE usuario (
  idusuario  serial PRIMARY KEY,
  nome varchar(255) NOT NULL unique,
  senha varchar(255) NOT NULL,
  criadoem date not null default CURRENT_DATE,
  alteradoem date not null default CURRENT_DATE,
  usuariocadastro varchar(255) NOT NULL,
  usuarioalteracao varchar(255)
);

insert into usuario (nome,senha,usuariocadastro) values('admin','pbkdf2:sha256:260000$oQ3eSha76K1m8q0i$b28b40156b2bd5aa154f5562f766b754dc5aaf859b8167eb313fa8ebc297889e','SISTEMA');