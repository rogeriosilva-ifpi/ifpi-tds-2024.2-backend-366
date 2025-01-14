from django.db import models
from sqlalchemy import false


class Montadora(models.Model):
  nome = models.CharField(max_length=128, blank=False, null=False)
  pais = models.CharField(max_length=128, blank=False, null=False)
  ano_fundacao = models.PositiveIntegerField()

  def __str__(self):
    return f'{self.nome} - {self.pais}'
  

MOTOR_CHOICES = (
  ('1.0', 'Motor 1.0'), 
  ('1.3', 'Motor 1.3'), 
  ('1.4', 'Motor 1.4'), 
  ('1.6', 'Motor 1.6'), 
  ('2.0', 'Motor 2.0')
)

class ModeloVeiculo(models.Model):
  nome = models.CharField(max_length=128, null=False, blank=False)
  motorizacao = models.CharField(choices=MOTOR_CHOICES, max_length=5, null=False, blank=False)

  # relacionamento
  montadora = models.ForeignKey(Montadora, 
                                on_delete=models.RESTRICT, 
                                related_name='veiculos')

  def __str__(self):
    return self.nome