from django.contrib import admin
from django.urls import path, include
# from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

admin.site.site_header = 'R1 Project Management'
admin.site.index_title = 'Operações'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('nucleo.urls')),
    path('api/token', TokenObtainPairView.as_view()),
    path('api/refresh-token', TokenRefreshView.as_view())
]
