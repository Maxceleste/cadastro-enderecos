from xml.parsers.expat import model
from django.db import models

# Create your models here.

class Endereco(models.Model):
    cep = models.CharField(max_length = 8)
    endereco = models.CharField(max_length=300)
    numero = models.CharField(max_length=50)
    complemento = models.CharField(max_length=300)
    bairro = models.CharField(max_length=300)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    descricao = models.CharField(max_length=300)