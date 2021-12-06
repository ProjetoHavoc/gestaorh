from django.db import models
from funcionarios.models import Funcionario

# Create your models here.

class Documentos(models.Model):
    
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return self.descricao
        