from django.urls import path
from nucleo.views import ProjetoListAPIView, \
                          EquipeListAPIView


# /api/projetos/
urlpatterns = [
  path('projetos', ProjetoListAPIView.as_view()),
  path('equipes', EquipeListAPIView.as_view()),
]