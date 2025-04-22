from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UsuarioViewSet, TarefaViewSet, LoginView

router = DefaultRouter()
router.register(r"usuarios", UsuarioViewSet)
router.register(r"tarefas", TarefaViewSet)

urlpatterns = router.urls + [
    path("login/", LoginView.as_view(), name="login"),
]
