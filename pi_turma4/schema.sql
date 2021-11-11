DROP TABLE IF EXISTS ponto;

CREATE TABLE ponto (
  idponto INTEGER PRIMARY KEY AUTOINCREMENT,
  titulo TEXT NOT NULL,
  descricao TEXT NOT NULL
);

DROP TABLE IF EXISTS usuario;

CREATE TABLE usuario (
  idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL UNIQUE,
  senha TEXT NOT NULL
);

insert into usuario (nome,senha) values('admin','pbkdf2:sha256:260000$oQ3eSha76K1m8q0i$b28b40156b2bd5aa154f5562f766b754dc5aaf859b8167eb313fa8ebc297889e');