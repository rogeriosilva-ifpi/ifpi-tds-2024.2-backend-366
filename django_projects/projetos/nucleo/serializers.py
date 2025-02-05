from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from nucleo.models import Projeto, Equipe, Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'


class EquipeBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = ['id', 'nome']





class ProjetoSerializer(serializers.ModelSerializer):
    equipe = EquipeBasicSerializer()

    class Meta:
        model = Projeto
        fields = ['id', 
                  'nome', 'data_inicio', 'data_fim', 
                  'orcamento', 'equipe']
        

class ProjetoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'data_inicio', 
                  'data_fim', 'orcamento']
        