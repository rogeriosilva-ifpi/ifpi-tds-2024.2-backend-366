from django.contrib import admin

from polls.models import Question

# Registrando um CRUD para Question
admin.site.register(Question)

