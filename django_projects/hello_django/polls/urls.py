from django.urls import path
from .views import index, polls_add

urlpatterns = [
  path('', index, name="index"),
  path('add', polls_add)
]