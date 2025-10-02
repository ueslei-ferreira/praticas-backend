from rest_framework import serializers
from .models import Urls

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = '__all__'