from rest_framework import serializers
from .models import CategoriaDespesas, Despesa, User

class CategoriaDespesasSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CategoriaDespesas
        fields = "__all__"
        
class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = "__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        return user