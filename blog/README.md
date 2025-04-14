# Personal Blogging Platform API

Este repositório contém uma API simples para gerenciar dados de blog pessoal com postagens chamadas de "artigos" e classes de artigos como "tag". Este projeto utiliza Django e Django REST Framework para criar uma API RESTful com operações CRUD.

## Funcionalidades da API

- **Artigos**:
  - Criar, listar, detalhar, atualizar e deletar artigos.
- **Tags**:
  - Criar e listar tags.
- **Relacionamento Artigo-Tag**:
  - Criar e listar relações entre artigos e tags.

## Tecnologias Utilizadas
- **Django**: Framework web para o backend.
- **Django REST Framework**: Para criar a API RESTful.
- **PostgreSQL**: Banco de dados relacional.
- **Python**: Linguagem de programação principal.

---

## O repositório está organizado da seguinte forma :
```bash

blog/
├── api/ # Arquivos do Django
├── artigos.sql # Arquivo SQL utilizado para criar as tabelas
├── manage.py 
├── README.md
├── requirements.txt # Dependências do projeto
└── REST API basics- CRUD, test & variable.postman_test_run.json # Coleção Postman para teste da API

```

## Estrutura do Projeto
- **Banco de Dados**: Criado com 3 tabelas (`artigos`, `tags`, `artigo_tag`) definidas no script SQL `artigos.sql`.
- **Models**: Gerados automaticamente com o comando `inspectdb` e ajustados para refletir as tabelas do banco.

---

## Como rodar o Projeto

### Pré-requisitos
- Python 3.12 ou superior
- PostgreSQL instalado e configurado
- Git instalado

### Passos para Configuração

1. **Clone o Repositório**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. **Crie e Ative o Ambiente Virtual**

```bash
python -m venv env
source env/bin/activate  # No Windows: .\env\Scripts\activate
```

3. **Instale as Dependências**
```bash
pip install -r requirements.txt

```
4. **Configure o Banco de Dados**

- Certifique-se de que o PostgreSQL está rodando.
- Crie um banco de dados chamado artigos (ou altere o nome no arquivo settings.py).
- Execute o script artigos.sql para criar as tabelas:

```bash
psql -U postgres -d artigos -f artigos.sql

```

5. **Aplique as Migrações**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Inicie o Servidor**

```bash
python manage.py runserver
```

## Testando a API

Para facilitar os testes da API, incluí um arquivo de coleção do Postman no repositório:  
`REST API basics- CRUD, test & variable.postman_test_run.json`.

### Como usar:

1. Abra o Postman.
2. Importe o arquivo de coleção localizado no repositório.
3. Certifique-se de que o servidor está rodando em `http://127.0.0.1:8000/`.
4. Execute as requisições disponíveis na coleção para testar os endpoints da API.

A coleção contém exemplos de requisições para criar, listar, atualizar e deletar artigos, tags e relações entre eles.