# Encurtador de URL

Este é um projeto de um encurtador de URL desenvolvido em Django e Django REST Framework.

## Funcionalidades

- Encurta URLs longas para URLs curtas e únicas.
- Redireciona de URLs curtas para as URLs longas originais.
- Normaliza as URLs para evitar duplicatas.
- Garante a unicidade das URLs curtas geradas.

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- PostgreSQL

## Configuração do Projeto

### Pré-requisitos

- Python 3.x
- PostgreSQL

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/ueslei-ferreira/praticas-backend/tree/main/6%20-%20encurta_URL
    cd \encurta_URL
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv env
    source env/bin/activate  # No Windows, use `env\Scripts\activate`
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```
    *(Observação: O arquivo `requirements.txt` não existe. Você precisará criá-lo com o conteúdo de `pip freeze`)*

4.  **Configure o banco de dados:**

    - Crie um banco de dados no PostgreSQL chamado `encurtador`.
    - Atualize as credenciais do banco de dados no arquivo `encurtador/settings.py`:

    ```python
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "encurtador",
            "USER": "seu-usuario",
            "PASSWORD": "sua-senha",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
    ```

5.  **Crie as tabelas do banco de dados:**

    Execute o seguinte script SQL para criar a tabela `urls`:

    ```sql
    CREATE TABLE urls (
        id SERIAL PRIMARY KEY,
        url_longo VARCHAR(1000) UNIQUE,
        url_curto VARCHAR(255) UNIQUE
    );

    CREATE UNIQUE INDEX idx_url_curto ON urls(url_curto);
    ```

6.  **Execute as migrações do Django:**

    ```bash
    python manage.py migrate
    ```

## Como Executar

1.  **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

2.  A aplicação estará disponível em `http://127.0.0.1:8000/`.

## Como Usar a API

### Encurtar uma URL

- **Endpoint:** `POST /api/encurtar/`
- **Body:**

  ```json
  {
      "url_longo": "https://www.sua-url-longa.com/aqui"
  }
  ```

- **Resposta de Sucesso (201 Created):**

  ```json
  {
      "id": 1,
      "url_longo": "https://www.sua-url-longa.com/aqui",
      "url_curto": "abcdef1"
  }
  ```

- **Resposta se a URL já existir (200 OK):**

  ```json
  {
      "id": 1,
      "url_longo": "https://www.sua-url-longa.com/aqui",
      "url_curto": "abcdef1"
  }
  ```

### Redirecionar

- **Endpoint:** `GET /<url_curto>/`
- **Exemplo:** `GET /abcdef1/`
- A aplicação irá redirecionar para a `url_longo` correspondente.
