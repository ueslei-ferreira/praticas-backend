from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Usuario, Tarefa


class UsuarioSerializer(serializers.ModelSerializer):
    data_criacao = serializers.DateField(read_only=True)

    class Meta:
        model = Usuario
        fields = "__all__"
        extra_kwargs = {"senha_hash": {"write_only": True}}

    def create(self, validated_data):
        validated_data["senha_hash"] = make_password(validated_data["senha_hash"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "senha_hash" in validated_data:
            validated_data["senha_hash"] = make_password(validated_data["senha_hash"])
        return super().update(instance, validated_data)


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = "__all__"

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    senha = serializers.CharField()
    
