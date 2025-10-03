from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UrlSerializer
from .models import Urls
from urllib.parse import urlparse, urlunparse
from django.shortcuts import redirect, get_object_or_404
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

def gerar_url_curto(hash: str, tamanho: int = 7) -> str:
    return hash[:tamanho]

def garantir_unicidade(url_curto: str) -> str:
    original = url_curto
    contador = 0
    while Urls.objects.filter(url_curto=url_curto).exists():
        contador += 1
        url_curto = original + str(contador)
    return url_curto

def redirect_view(request, url_curto):
    url_obj = get_object_or_404(Urls, url_curto=url_curto)
    return redirect(url_obj.url_longo)

class UrlView(viewsets.ModelViewSet):
    queryset = Urls.objects.all()
    serializer_class = UrlSerializer
    
    def create(self, request, *args, **kwargs):
        
        url_longo = request.data.get('url_longo')
        
        if not url_longo:
            return Response({"error": "url_longo é necessária"},status=status.HTTP_400_BAD_REQUEST)
        
        url_longo = normalizar_url(url_longo)
        
        existente = Urls.objects.filter(url_longo = url_longo).first()
        if existente:
            serializer = self.get_serializer(existente)
            return Response(serializer.data, status.HTTP_200_OK)
        
        hash_url = gerar_hash(url_longo)
        url_curto = gerar_url_curto(hash_url)
        url_curto = garantir_unicidade(url_curto)
        
        serializer = self.get_serializer(data={"url_longo": url_longo, "url_curto":url_curto})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)