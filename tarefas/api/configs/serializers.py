from rest_framework import serializers
from .models import Usuario, Tarefa

class UsuarioSerializer(serializers.ModelSerializer):
    data_criacao = serializers.DateField(read_only=True)
    class Meta:
        model = Usuario
        fields = "__all__"
        
class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = "__all__"
        
    