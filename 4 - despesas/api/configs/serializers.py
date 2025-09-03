from rest_framework import serializers
from .models import User, CategoriaDespesas, Despesa

class CategoriaDespesasSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CategoriaDespesas
        fields = "__all__"
        
class DespesasSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # leitura: objeto aninhado
    tipo_despesas = CategoriaDespesasSerializer(read_only=True)

    # escrita: envie "tipo_despesas_id": <id>
    tipo_despesas_id = serializers.PrimaryKeyRelatedField(
        source='tipo_despesas',
        queryset=CategoriaDespesas.objects.all(),
        write_only=True,
        required=True
    )

    class Meta:
        model = Despesa
        fields = ("id", "vencimento", "descricao", "montante", "user", "tipo_despesas", "tipo_despesas_id")
        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # usa create_user para garantir hashing
        user = User.objects.create_user(password=password, **validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # garante hash
        instance.save()
        return instance