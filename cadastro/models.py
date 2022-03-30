from xml.parsers.expat import model
from django.db import models

# Create your models here.

class enderecos(models.Model):
    cep = models.CharField(max_length = 8)
    endereco = models.TextField()
    numero = models.CharField(max_length=50)
    complemento = models.TextField()
    bairro = models.TextField()
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    descricao = models.TextField()