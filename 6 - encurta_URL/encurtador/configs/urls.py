from rest_framework.routers import DefaultRouter
from .views import UrlView

router = DefaultRouter()

router.register(r'encurtar', UrlView, basename='encurtar')

urlpatterns = router.urls