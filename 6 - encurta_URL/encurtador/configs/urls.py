from rest_framework.routers import DefaultRouter
from .views import UrlViewSet

router = DefaultRouter()

router.register(r'encurtar', UrlViewSet, basename='encurtar')

urlpatterns = router.urls