CREATE TABLE categoria_despesas(
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO categoria_despesas (tipo) VALUES ("mercado"),("lazer"),("eletrônicos"),("saúde"),("roupas"),("outros");

CREATE TABLE despesa(
    id SERIAL PRIMARY KEY,
    vencimento DATE,
    montante DECIMAL(10,2),
    tipo_despesas_id INT NOT NULL references categoria_despesas(id),
);