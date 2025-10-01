from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UrlSerializer
from .models import Urls

class UrlView(viewsets.ModelViewSet):
    queryset = Urls.objects.all()
    serializer_class = UrlSerializer
    
    def create(self, request, *args, **kwargs):
        
        url_longo = request.data.get('url_longo')
        
        existente = Urls.objects.filter(url_longo = url_longo).first
        if existente:
            serializer = self.get_serializer(existente)
            return Response(serializer.data, status.HTTP_200_OK)
        
        serializer = self.get_serializer(data={"url_longo": url_longo})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)