Esse projeto visou construir minha própria API para consumir uma API de terceiros, com informações sobre clima e tempo. Com foco em cache, utilizando redis, a API foi construída utilizando django.

Pontos importantes aprendidos: Variáveis de ambiente para maior privacidade, como receber os dados das requisições por 'JSON' ou 'URL', uso de cache com Redis, integração com Docker, e boas práticas de organização de código.

A API de terceiros utilizada pode ser encontrada em: https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/

Se desejar testar localmente, crie uma conta para obter sua chave de API no site acima, e coloque na variável abiente: 'API_KEY'.

---

## Passos para construir este projeto

1. **Criação do ambiente e estrutura do projeto**
   - Criação de um ambiente virtual Python.
   - Instalação do Django e Django REST Framework.
   - Inicialização do projeto Django e criação do app principal.

2. **Configuração do controle de dependências**
   - Instalação de dependências adicionais: `requests`, `python-dotenv`, `redis`, `django-redis`.
   - Geração do arquivo `requirements.txt` com `pip freeze > requirements.txt`.

3. **Uso de variáveis de ambiente**
   - Criação do arquivo `.env` para armazenar informações sensíveis como a API KEY e configurações do Redis.
   - Uso do pacote `python-dotenv` para carregar as variáveis de ambiente no código.

4. **Implementação da view principal**
   - Criação de uma view baseada em classe (`APIView`) para receber requisições POST com cidade ou latitude/longitude.
   - Montagem dinâmica da URL para a API de clima de terceiros.
   - Recebimento de dados tanto por JSON quanto por parâmetros de URL.

5. **Implementação do cache com Redis**
   - Criação de um módulo utilitário para abstrair o uso do Redis (`server_redis/weather_cache.py`).
   - Configuração do Redis para rodar em container Docker.
   - Uso das funções `get_cache` e `set_cache` para armazenar e recuperar dados do cache.

6. **Configuração do Docker e Redis**
   - Instalação do Docker Desktop.
   - Execução do Redis em container Docker com o comando:
     ```
     docker run -d -p 6379:6379 --name redis redis
     ```
   - Configuração das variáveis `REDIS_HOST` e `REDIS_PORT` no `.env`.

7. **Tratamento de erros e boas práticas**
   - Adição de tratamento para erros de conexão, respostas inválidas da API externa e falhas de cache.
   - Impressão de logs para facilitar o debug.

8. **Testes e validação**
   - Testes das rotas usando ferramentas como Postman ou curl.
   - Validação do funcionamento do cache (primeira requisição busca na API, próximas usam o Redis).

---

## Como rodar o projeto

1. Instale as dependências:# Instale as dependências do Python
pip install -r requirements.txt

# Inicie o Redis usando Docker
docker run -d -p 6379:6379 --name redis redis

# Crie o arquivo .env na raiz do projeto com o seguinte conteúdo:
# (edite sua chave da API)
"API_KEY= "sua_chave_aqui"
REDIS_HOST=localhost
REDIS_PORT=6379" > .env

# Rode o servidor Django
python manage.py runserver

### Testando a API de Clima com Postman

1. **Abra o Postman**

2. **Crie uma nova requisição**
   - Método: `POST`
   - URL:
     ```
     http://localhost:8000/weather/
     ```

3. **No corpo da requisição (Body)**
   - Selecione **raw** e escolha **JSON**.
   - Exemplo de corpo para cidade:
     ```json
     {
       "cidade": "Brasilia"
     }
     ```
   - Ou para latitude/longitude:
     ```json
     {
       "latitude": -15.793889,
       "longitude": -47.882778
     }
     ```

4. **Envie a requisição**
   - Clique em **Send**.

Você verá a resposta da sua API, que pode vir do cache (Redis) ou da API externa, dependendo se já existe cache para a consulta.
