from django.contrib import admin
from django.urls import path, include
# from django.http import HttpResponse

admin.site.site_header = 'R1 Project Management'
admin.site.index_title = 'Operações'

from nucleo.views import ProjetoListAPIView

# def listar_projetos(request):
#   return HttpResponse('Lista de projetos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('nucleo.urls')),
]
