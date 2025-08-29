CREATE TABLE artigos (
    id SERIAL PRIMARY KEY,
    titulo varchar(255) NOT NULL,
    conteudo text NOT NULL,
    slug varchar(255) NOT NULL,
    data_criacao date NOT NULL DEFAULT CURRENT_TIMESTAMP,
    publicado boolean NOT NULL DEFAULT false
);

CREATE TABLE tag(
    id SERIAL PRIMARY KEY,
    nome varchar(255) NOT NULL
);

CREATE TABLE artigo_tag(
    id SERIAL PRIMARY KEY,
    artigo_id int NOT NULL,
    tag_id int NOT NULL,
    FOREIGN KEY (artigo_id) REFERENCES artigos(id),
    FOREIGN KEY (tag_id) REFERENCES tag(id)
);