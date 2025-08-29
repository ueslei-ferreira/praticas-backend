import os
import json
import redis
from dotenv import load_dotenv

load_dotenv()

r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    db=0,
    decode_responses=True
)

def get_cache(key):
    """Retorna o valor desserializado ou None."""
    val = r.get(key)
    return json.loads(val) if val else None

def set_cache(key, data, exp=600):
    """Serializa e salva no Redis com expiração (default 10min)."""
    r.set(key, json.dumps(data), ex=exp)
