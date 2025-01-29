from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField('Descrição')
    data_inicio = models.DateField('Data de Início')
    data_fim = models.DateField('Data de Fim')
    orcamento = models.DecimalField('Orçamento', max_digits=10, decimal_places=2)

    equipe = models.ForeignKey('Equipe', 
                               on_delete=models.CASCADE, 
                               related_name='projetos',
                               null=True, blank=True)

    def __str__(self):
        return self.nome
    

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
    def total_membros(self):
        return self.membros.count()
    

SEXO_CHOICES = (('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'))

class Membro(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, default='O', choices=SEXO_CHOICES)
    telefone = models.CharField(
      max_length=15, 
      help_text='(99) 99999-9999',
      validators=[RegexValidator(regex=r'^\(\d{2}\) \d{5}-\d{4}$', 
                                 message='Telefone deve estar no formato (99) 99999-9999')]
    )
    ativo = models.BooleanField(default=True)

    equipe = models.ForeignKey('Equipe', 
                               on_delete=models.CASCADE, 
                               related_name='membros',
                               null=True, blank=True)

    def __str__(self):
        return f'{self.nome} ({self.equipe}))'
    

class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField('Descrição', max_length=500, null=True, blank=True)
    data_inicio = models.DateField('Data de Início')
    data_fim = models.DateField('Data de Fim', null=True, blank=True)
    horas_estimadas = models.DecimalField('Horas Estimadas', max_digits=5, decimal_places=2)

    projeto = models.ForeignKey('Projeto', 
                                on_delete=models.CASCADE, 
                                related_name='atividades')
    membro = models.ForeignKey('Membro',
                               on_delete=models.SET_NULL,
                               related_name='atividades',
                               null=True, blank=True)
    
    def clean(self):
      if self.data_fim < self.data_inicio:
        raise ValidationError('Data de fim deve ser após data de início ou igual')
      
    def clean_horas_estimadas(self):
      if self.horas_estimadas <= 0:
        raise ValidationError('Horas estimadas deve ser maior que zero')
      
    def clean_membro(self):
      if self.membro.equipe != self.projeto.equipe:
        raise ValidationError('Membro deve pertencer à equipe do projeto')

    def __str__(self):
        return self.nome
  
