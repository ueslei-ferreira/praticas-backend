# Notes API (Django + DRF)

API simples para criar/armazenar notas em Markdown, renderizar em HTML e checar gramática (pt-BR).

## Estrutura principal
- app: `api.configs`
- modelo `Note` (fields principais): `title`, `content` (markdown)
- endpoints principais:
  - `GET  /api/notes/` — listar notas
  - `POST /api/notes/` — criar nota (JSON ou multipart/form-data com upload de arquivo .md)
  - `GET  /api/notes/<id>/render/` — retorna HTML renderizado da nota
  - `POST /api/notes/check_grammar/` — checa gramática (pt-BR) para um texto

OBS: o view atual lê o arquivo enviado (`file`) e grava seu conteúdo em `content` — o arquivo não é salvo no filesystem por padrão.

## Requisitos
- Python 3.11+
- virtualenv
- Dependências 

```
  pip install `requirements.txt`

```

## Setup (PowerShell / Windows)
1. Ativar virtualenv:
   python -m venv env
   .\env\Scripts\Activate.ps1

2. Instalar dependências:
   pip install -r requirements.txt

3. Rodar migrações:
   python manage.py migrate

4. Rodar servidor:
   python manage.py runserver

5. Executar testes:
   python manage.py test

## Como testar com Postman
1. Abra Postman → Import → File → selecione a coleção (ex.: `postman/notes-api.postman_collection.json`) 
2. Endpoints:

- Criar nota (JSON)
  - Método: POST
  - URL: `http://127.0.0.1:8000/api/notes/`
  - Body → raw → JSON
  - Exemplo:
    {
      "title": "Minha nota",
      "content": "# Título\nConteúdo em markdown"
    }

- Criar nota (upload de arquivo .md)
  - Método: POST
  - URL: `http://127.0.0.1:8000/api/notes/`
  - Body → form-data
    - key: `title` (Text)
    - key: `file` (File) → selecione `.md`
  - Se `content` também for enviado como campo de texto, o upload é ignorado (o view prioriza `content` se presente).

- Renderizar nota para HTML
  - Método: GET
  - URL: `http://127.0.0.1:8000/api/notes/<id>/render/`

- Checar gramática
  - Método: POST
  - URL: `http://127.0.0.1:8000/api/notes/check_grammar/`
  - Body → raw → JSON
    { "content": "Texto a checar" }

