from django.urls import path
from .views import ArtigosListCreateView, ArtigosDetailView, TagListCreateView, ArtigoTagListCreateView

urlpatterns = [
    path('artigos/', ArtigosListCreateView.as_view(), name='artigos-list-create'),
    path('artigos/<int:pk>/', ArtigosDetailView.as_view(), name='artigos-detail'),
    path('tags/', TagListCreateView.as_view(), name='tags-list-create'),
    path('artigo-tags/', ArtigoTagListCreateView.as_view(), name='artigo-tags-list-create'),
]