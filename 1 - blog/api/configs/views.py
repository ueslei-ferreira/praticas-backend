
from rest_framework import generics, filters
from .models import Artigos, Tag, ArtigoTag
from .serializers import ArtigosSerializer, TagSerializer, ArtigoTagSerializer
from rest_framework.response import Response
from rest_framework import status


# Listar e criar artigos
class ArtigosListCreateView(generics.ListCreateAPIView):
    queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'conteudo']

    # metodo que possibilita a criação de vários artigos de uma vez por meio de um array
    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# Detalhar, atualizar e deletar um artigo
class ArtigosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer


# Listar e criar tags
class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # metodo que possibilita a criação de vários artigos de uma vez por meio de um array
    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# Listar e criar relações entre artigos e tags
class ArtigoTagListCreateView(generics.ListCreateAPIView):
    queryset = ArtigoTag.objects.all()
    serializer_class = ArtigoTagSerializer

    # metodo que possibilita a criação de vários artigos de uma vez por meio de um array
    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
