# your_app/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import os
from django.conf import settings
from cliente_redis.weather_cache import get_cache, set_cache

class WeatherView(APIView):
    def post(self, request):
        cidade   = request.data.get('cidade')
        latitude = request.data.get('latitude')
        longitude= request.data.get('longitude')

        if cidade:
            location = cidade
        elif latitude and longitude:
            location = f"{latitude},{longitude}"
        else:
            return Response(
                {'error': 'Informe cidade ou latitude e longitude'},
                status=400
            )

        key = f"weather_{location.lower()}"
        # 1) tenta do cache
        data = get_cache(key)
        if data:
            return Response(data)

        # 2) busca na API externa
        api_key = settings.API_KEY
        url = (
            f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={api_key}'
        )
        resp = requests.get(url)
        
        try:
            data = resp.json()
        except Exception as e:
            return Response({
                'error': 'Erro ao decodificar JSON',
                'detalhe': str(e),
                'resposta': resp.text
            }, status=500)

        # 3) salva no cache
        set_cache(key, data)

        return Response(data)
