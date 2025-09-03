# Backend - Despesas

API Django / Django REST Framework para gerenciar categorias de despesas, despesas e usuários (autenticação via JWT).

## Estrutura principal
- api/ — app Django principal
  - configs/
    - models.py — modelos: `CategoriaDespesas`, `Despesa`, `User` (User custom)
    - serializers.py — serializers para `CategoriaDespesas`, `Despesa`, `User`
    - views.py — viewsets: `DespesaView`, `CategoriaDespesasView`, `UserView` (possui action `vencimento`)
    - urls.py — registra routes via `DefaultRouter`
  - settings.py, urls.py, wsgi/asgi.py

## Requisitos
- Python 3.10+ (usando 3.12 no projeto)
- Django
- djangorestframework
- djangorestframework-simplejwt
- python-dotenv (se usar .env)
- psycopg2-binary (Postgres)

Instalar requirements:
```powershell
pip install requirements.txt
```

## Configuração (Windows)
1. Criar e ativar venv:
   - python -m venv venv
   - venv\Scripts\activate

2. Instalar dependências:
   - pip install -r requirements.txt

3. Variáveis de ambiente (ex.: arquivo `.env` na raiz do projeto)
```env
SECRET_KEY=troque_esta_chave
DEBUG=True
DB_NAME=seu_db
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```
Se usar `python-dotenv`, carregue no settings.py com `load_dotenv()`.

4. Migrar/atualizar banco:
   - python manage.py migrate
   - (se necessário) python manage.py makemigrations

5. Criar superuser (opcional):
   - python manage.py createsuperuser

6. Rodar servidor:
   - python manage.py runserver

## Endpoints principais
(assumindo prefixo `/api/` na URL root)

- /api/despesa/ — ViewSet `DespesaView`
  - GET list / POST create / PUT/PATCH / DELETE
  - Para criar (`POST`) o corpo deve conter:
    ```json
    {
      "descricao": "mouse novo",
      "vencimento": "2025-09-21",
      "montante": "170.50",
      "tipo_despesas_id": 2
    }
    ```
  - O serializer retorna o objeto aninhado `tipo_despesas` (categoria) no GET.

- /api/despesa/vencimento/?start=YYYY-MM-DD&end=YYYY-MM-DD
  - Action `vencimento` no `DespesaView` — filtra despesas cujo campo `vencimento` está no intervalo [start, end].
  - Exemplo:
    - GET /api/despesa/vencimento/?start=2025-09-01&end=2025-09-30

- /api/categoria/ — `CategoriaDespesasView` (CRUD categorias)
- /api/usuario/ — `UserView` (cria usuário; a criação atual retorna tokens JWT)

## Autenticação
- JWT (djangorestframework-simplejwt)
- Criando usuário via `/api/usuario/` a resposta inclui `refresh` e `access` (conforme implementação atual).
- Usar header:
  - Authorization: Bearer <access_token>

Exemplo curl (Windows PowerShell):
```powershell
curl -X GET "http://localhost:8000/api/despesa/vencimento/?start=2025-09-01&end=2025-09-30" -H "Authorization: Bearer <TOKEN>"
```

## Observações e dicas
- O campo FK em `Despesa` chama-se `tipo_despesas`. Para criação use `tipo_despesas_id`.
- A action `vencimento` atualmente usa query params (GET). Se preferir enviar JSON no corpo, é possível aceitar POST e ler `request.data`.
- Alguns modelos estão com `managed = False` — tenha cuidado ao usar migrações se o banco já existir.
- Se aparecer erro "Import 'dotenv' could not be resolved", instale `python-dotenv` no venv e selecione o interpretador correto no VS Code.

## Testes
- `python manage.py test` — adiciona/implementa testes em `api/configs/tests.py`.

## Contribuição
- Abrir issues/pull requests para bugs e melhorias.
- Código organizado em `api/configs/` — alterações em serializers/views devem considerar autenticação