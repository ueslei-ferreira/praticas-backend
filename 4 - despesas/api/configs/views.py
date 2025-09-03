from rest_framework import viewsets, status, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .models import *
from datetime import date

class DespesaView(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesasSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated], url_path='vencimento')
    def vencimento(self, request):
        """
        GET /api/despesa/vencimento/?start=YYYY-MM-DD&end=YYYY-MM-DD
        Retorna apenas despesas do usuário autenticado com vencimento entre start e end (inclusive).
        'start' e 'end' são obrigatórios.
        """
        start = request.query_params.get('start')
        end = request.query_params.get('end')
        if not start or not end:
            return Response(
                {"detail": "Parâmetros 'start' e 'end' são obrigatórios (formato YYYY-MM-DD)."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            start_date = date.fromisoformat(start)
            end_date = date.fromisoformat(end)
        except ValueError:
            return Response({"detail": "Formato inválido. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        if start_date > end_date:
            return Response({"detail": "'start' deve ser menor ou igual a 'end'."}, status=status.HTTP_400_BAD_REQUEST)

        qs = self.get_queryset().filter(vencimento__gte=start_date, vencimento__lte=end_date)
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

    @action(detail=False, methods=['get', 'put', 'patch'], permission_classes=[IsAuthenticated])
    def me(self, request):
        # GET: retorna os dados do usuário logado
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)

        # PUT/PATCH: atualiza somente o usuário autenticado
        partial = request.method == 'PATCH'
        serializer = self.get_serializer(request.user, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # Protege update/partial_update para que só admin ou dono possam alterar outro usuário
    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if not (request.user.is_staff or request.user == obj):
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        obj = self.get_object()
        if not (request.user.is_staff or request.user == obj):
            return Response({'detail': 'Não autorizado.'}, status=status.HTTP_403_FORBIDDEN)
        return super().partial_update(request, *args, **kwargs)

