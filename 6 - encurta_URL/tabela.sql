CREATE TABLE urls (
    id SERIAL PRIMARY KEY,
    url_longo VARCHAR(1000) UNIQUE,
    url_curto VARCHAR(255) UNIQUE
);

CREATE UNIQUE INDEX idx_url_curto ON urls(url_curto);

--como usar o index de url longo
SELECT url_longo FROM urls WHERE url_curto= 'abc123';
