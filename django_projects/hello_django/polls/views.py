from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return HttpResponse("Hello World. Polls index!!!")


def polls_add(request):
  return HttpResponse("Nova enquete!!")
