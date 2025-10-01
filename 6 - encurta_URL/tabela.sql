CREATE TABLE urls (
    id SERIAL PRIMARY KEY,
    url_longo VARCHAR(1000),
    url_curto VARCHAR(255) UNIQUE
);

CREATE UNIQUE INDEX idx_url_longo ON urls(url_longo);

--como usar o index de url longo
SELECT url_curto FROM urls WHERE url_longo= 'abc123';
