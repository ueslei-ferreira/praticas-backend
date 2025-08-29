from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .models import *

class DespesaView(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesasSerializer
    
class CategoriaDespesasView(viewsets.ModelViewSet):
    queryset = CategoriaDespesas.objects.all()
    serializer_class = CategoriaDespesasSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list', 'destroy']:
            perms = [IsAdminUser]
        elif self.action in ['retrieve', 'update', 'partial_update', 'me']:
            perms = [IsAuthenticated]
        else:
            perms = []
        return [p() for p in perms]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = serializer.data
        data.update({'refresh': str(refresh), 'access': str(refresh.access_token)})
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


