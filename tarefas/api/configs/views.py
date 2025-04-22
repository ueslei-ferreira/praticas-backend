from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password

from .models import Usuario, Tarefa
from .serializers import UsuarioSerializer, TarefaSerializer, LoginSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class LoginView(APIView):
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username =  serializer.validated_data['username']
            senha =  serializer.validated_data['senha']
            
            try:
                usuario = Usuario.objects.get(username=username)
            except Usuario.DoesNotExist:
                return Response({"erro": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

            if check_password(senha, usuario.senha_hash):
                # Aqui você pode retornar um token ou os dados do usuário
                return Response({"mensagem": "Login bem-sucedido",
                                 "usuario": usuario.id})
            else:
                return Response({"erro": "Senha incorreta"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)