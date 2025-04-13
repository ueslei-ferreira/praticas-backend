# Personal Blogging Platform API

Uma API para gerenciar dados de blog pessoal com postagens chamadas de "artigos" e classes de artigos como "tag". Este projeto utiliza Django e Django REST Framework para criar uma API RESTful com operações CRUD.

## Tecnologias Utilizadas
- **Django**: Framework web para o backend.
- **Django REST Framework**: Para criar a API RESTful.
- **PostgreSQL**: Banco de dados relacional.
- **Python**: Linguagem de programação principal.

---

## Estrutura do Projeto
- **Banco de Dados**: Criado com 3 tabelas (`artigos`, `tags`, `artigo_tag`) definidas no script SQL `artigos.sql`.
- **Models**: Gerados automaticamente com o comando `inspectdb` e ajustados para refletir as tabelas do banco.

---
