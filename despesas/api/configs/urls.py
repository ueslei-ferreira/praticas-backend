from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import DespesaView, CategoriaDespesasView, UserView

router = DefaultRouter()

router.register(r"despesa", DespesaView)
router.register(r"categoria", CategoriaDespesasView)
router.register(r"usuario", UserView, basename="user")

urlpatterns = router.urls
