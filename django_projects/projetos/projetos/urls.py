from django.contrib import admin
from django.urls import path

admin.site.site_header = 'R1 Project Management'
admin.site.index_title = 'Operações'

urlpatterns = [
    path('admin/', admin.site.urls),
]
