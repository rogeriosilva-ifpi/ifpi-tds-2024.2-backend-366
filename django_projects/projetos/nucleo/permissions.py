from email import message
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import status

class MyRogerPermissions(BasePermission):
  message = 'Somente para Rogers!'

  def has_permission(self, request, view):
    # codigo para deixar ou não passar
    user = request.user
    print(user.username)
    if 'roger' not in user.username:
      return False
    # print('passou por aqui...HAS_PERMISSION')
    return super().has_permission(request, view)
  
  def has_object_permission(self, request, view, obj):
    # print('passou por aqui...HAS_OBJ_PERMISSION')
    # print(obj)
    return super().has_object_permission(request, view, obj)