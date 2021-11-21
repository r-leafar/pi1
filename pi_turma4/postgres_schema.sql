DROP TABLE IF EXISTS ponto;

CREATE TABLE ponto (
  idponto serial PRIMARY KEY,
  titulo varchar(255) NOT NULL,
  descricao TEXT NOT NULL,
  nomeimg varchar(255) NOT NULL,
  tipoponto smallint not null,
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

INSERT INTO usuario (nome,senha,usuariocadastro) values('admin','pbkdf2:sha256:260000$oQ3eSha76K1m8q0i$b28b40156b2bd5aa154f5562f766b754dc5aaf859b8167eb313fa8ebc297889e','SISTEMA');

INSERT INTO ponto(titulo,descricao,nomeimg,tipoponto,usuariocadastro) VALUES ('PEDRA DA FREIRA','Um local cercado de mistérios bem perto do centro de Caraguatatuba. Os moradores do local contam que segundo a lenda, a tal freira era apaixonada por um pescador e todos os dias o esperava regressar do mar com seus peixes. Mas um dia, ele não voltou da pescaria e ela teria virado pedra de tanto esperar o retorno de seu amado.','1.jpg',1,'SISTEMA');

INSERT INTO ponto(titulo,descricao,nomeimg,tipoponto,usuariocadastro) VALUES ('PRAIA DO PORTO NOVO','Possui águas tranquilas, quase sem ondas e uma larga faixa de areia ideal para caminhadas e prática de esportes. Nessa praia desemboca o rio Juqueriquerê que faz a divisa de Caraguatatuba com São Sebastião. Próximo à foz do rio há uma área de mangue onde podem ser observadas de perto algumas aves marinhas como Garças e Atobás. Fica 9 km ao sul do centro.','2.jpg',1,'SISTEMA');

INSERT INTO ponto(titulo,descricao,nomeimg,tipoponto,usuariocadastro) VALUES ('IGREJA MATRIZ DE SANTO ANTÔNIO','A História do município de Caraguatatuba, começa junto com a construção da Capela de Santo Antônio padroeiro da cidade. Em 1600, foi fundada a (Vila de Santo Antonio de Caraguatatuba), e somente em 1857 foi elevado a categoria de município. No ano de 1870, as obras da então Igreja Matriz foi concluída, e foi entregue para autoridades começarem os serviços religiosos. Atualmente as paredes da igreja estão pintadas de branco com faixas azul, seguindo o estilo de construções dos "Padres Jesuítas" da época da colonização do Brasil. A sua fachada é simples,com 1 porta de entrada, e 3 janelas acima, sua torre é muito bonita com um sino elegante. No seu interior, as paredes laterais foram construídas em formato de arcos, com belíssimas pinturas no alto. O altar principal e uma parte do forro da igreja, foi todo trabalhado e esculpido em madeira, deixando o ambiente totalmente elegante. A Igreja Matriz está localizada na Praça Cândido Motta no centro de Caraguatatuba.','3.jpg',2,'SISTEMA');
