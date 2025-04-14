from rest_framework import serializers
from .models import Artigos, Tag, ArtigoTag


class ArtigosSerializer(serializers.ModelSerializer):
    data_criacao = serializers.DateField(read_only=True)
    
    class Meta:
        model = Artigos
        fields = "__all__"
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ArtigoTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtigoTag
        fields = "__all__"
