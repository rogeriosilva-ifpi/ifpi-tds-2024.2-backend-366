from django.urls import path, include
from nucleo.views import ProjetoListAPIView #, \
                          # EquipeListAPIView
from nucleo.views import EquipeListCreateView, EquipeDetailView, ComentarioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'comentarios', ComentarioViewSet)
# registrar vários viewsets/recursos

# /api/projetos/
urlpatterns = [
  path('projetos', ProjetoListAPIView.as_view()),
  path('equipes', EquipeListCreateView.as_view()),
  path('equipes/<int:pk>', EquipeDetailView.as_view()),
  # path('equipes', EquipeListAPIView.as_view()),
  path('', include(router.urls)),
]