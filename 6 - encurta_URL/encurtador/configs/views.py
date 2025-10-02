from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UrlSerializer
from .models import Urls
from urllib.parse import urlparse, urlunparse
import hashlib

def normalizar_url(url: str) -> str:
    url = url.strip()
    parsed = urlparse(url)

    esquema = parsed.scheme.lower()
    dominio = parsed.netloc.lower()

    path = parsed.path or ""
    if path.endswith("/") and path != "/":
        path = path[:-1]

    return urlunparse((
        esquema,
        dominio,
        path,
        parsed.params,
        parsed.query,
        parsed.fragment
    ))
def gerar_hash(url: str) -> str:
    hash_completo = hashlib.sha256(url.encode('utf-8'))
    return hash_completo.hexdigest()
def gerar_url_curta(hash: str, tamanho: int = 7) -> str:
    return hash[:tamanho]

def garantir_unicidade(url_curta: str) -> str:
    original = url_curta
    contador = 0
    while Urls.objects.filter(url_curta=url_curta).exists():
        contador += 1
        url_curta = original + str(contador)
    return url_curta

class UrlView(viewsets.ModelViewSet):
    queryset = Urls.objects.all()
    serializer_class = UrlSerializer
    
    def create(self, request, *args, **kwargs):
        
        url_longa = request.data.get('url_longa')
        
        if not url_longa:
            return Response({"error": "url_longa é necessária"},status=status.HTTP_400_BAD_REQUEST)
        
        url_longa = normalizar_url(url_longa)
        
        existente = Urls.objects.filter(url_longa = url_longa).first()
        if existente:
            serializer = self.get_serializer(existente)
            return Response(serializer.data, status.HTTP_200_OK)
        
        hash_url = gerar_hash(url_longa)
        url_curta = gerar_url_curta(hash_url)
        url_curta = garantir_unicidade(url_curta)
        
        serializer = self.get_serializer(data={"url_longa": url_longa, "url_curta":url_curta})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)