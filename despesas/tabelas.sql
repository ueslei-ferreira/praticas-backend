CREATE TABLE tarefa(
    id SERIAL PRIMARY KEY,
    categoria VARCHAR(100) NOT NULL,
    vencimento DATE,
    montante DECIMAL(10,2)
);