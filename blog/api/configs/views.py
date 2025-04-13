from django.shortcuts import render
from rest_framework import generics
from .models import Artigos, Tag, ArtigoTag
from .serializers import ArtigosSerializer, TagSerializer, ArtigoTagSerializer


# Listar e criar artigos
class ArtigosListCreateView(generics.ListCreateAPIView):
    queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer


# Detalhar, atualizar e deletar um artigo
class ArtigosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer


# Listar e criar tags
class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# Listar e criar relações entre artigos e tags
class ArtigoTagListCreateView(generics.ListCreateAPIView):
    queryset = ArtigoTag.objects.all()
    serializer_class = ArtigoTagSerializer
