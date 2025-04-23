from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import AllowAny, BasePermission
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

from .models import Usuario, Tarefa
from .serializers import UsuarioSerializer, TarefaSerializer, LoginSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    Permite criar, listar, atualizar e deletar usuários.
    Apenas a criação (register) é aberta para não autenticados.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.action == "create": 
            return [AllowAny()]
        return super().get_permissions()
    

class SessaoUsuarioPermission(BasePermission):
    """
    Permissão customizada que permite acesso apenas se houver 'usuario_id' na sessão.
    Usada para proteger endpoints que exigem login pelo sistema próprio.
    """
    def has_permission(self, request, view):
        return bool(request.session.get('usuario_id'))

@method_decorator(ensure_csrf_cookie, name='dispatch')
class TarefaViewSet(viewsets.ModelViewSet):
    """
    Permite criar, listar, atualizar e deletar tarefas.
    Só permite acesso se o usuário estiver autenticado via sessão customizada.
    """
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [SessaoUsuarioPermission]

    

@method_decorator(ensure_csrf_cookie, name='dispatch')
class LoginView(APIView):
    """
    Realiza o login do usuário.
    Se as credenciais estiverem corretas, salva o 'usuario_id' na sessão.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            senha = serializer.validated_data['senha']

            try:
                usuario = Usuario.objects.get(username=username)
            except Usuario.DoesNotExist:
                return Response({"erro": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

            if check_password(senha, usuario.senha_hash):
                # Crie um objeto de usuário autenticável para o Django
                class SimpleUser:
                    def __init__(self, id, username):
                        self.id = id
                        self.username = username
                        self.is_authenticated = True
                user = SimpleUser(usuario.id, usuario.username)
                request.user = user
                # Salve o id na sessão para manter compatibilidade com seu código
                request.session['usuario_id'] = usuario.id
                return Response({
                    "mensagem": "Login bem-sucedido",
                    "usuario_id": usuario.id
                }, status=status.HTTP_200_OK)
            else:
                return Response({"erro": "Senha incorreta"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TarefasPorUsuarioView(APIView):
    """
    Retorna todas as tarefas relacionadas a um usuário específico (filtrando por usuario_id).
    """
    def get(self, request, usuario_id):
        tarefas = Tarefa.objects.filter(usuario_id=usuario_id)
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)
