from termios import CEOF
from xml.parsers.expat import model
from django import forms
from django.db import models
from django.forms import ModelForm
from django.core.validators import RegexValidator


# Create your models here.

class Endereco(models.Model):
#Todo a estrutura do banco de dados criada aqui, considerando alguns valores para que não inserir endereços errados.

    cep = models.CharField(
        verbose_name = 'CEP',
        max_length = 8 ,
        help_text='Ex: 36202072',
        validators=[ RegexValidator(r'^\d\d\d\d\d\d\d\d$', message = 'Insira um CEP válido')  ], 
        error_messages = {'required' : 'Por favor, insira o CEP', 'max_lenght' : 'O CEP deve conter 8 números.' }
    )

    endereco = models.CharField(
        max_length = 300,
        verbose_name = 'Endereço',
        help_text = 'Ex: José Josino de Oliveira',
        error_messages = {'required' : 'Por favor, insira o endereço', 'max_lenght' : 'O endereço é muito grande.'}
    )

    numero = models.CharField(
        verbose_name = 'Número',
        max_length = 15,
        help_text = 'Ex: 45',
        error_messages = {'required' : 'Por favor, insira o número', 'max_lenght' : 'O número é muito grande.'}
    )

    complemento = models.CharField(
        verbose_name = 'Complemento (Não obrigatório)',
        max_length = 300,
        help_text = 'Ex: Casa 2',
        error_messages = {'max_lenght' : 'O complemento é muito grande.'},
        blank = True
    )

    bairro = models.CharField(
        verbose_name = 'Bairro',
        max_length = 300,
        help_text = 'Ex: Funcionários',
        error_messages = {'required' : 'Por favor, insira o bairro', 'max_lenght' : 'O bairro é muito grande.'}
    )

    cidade = models.CharField(
        verbose_name = 'Cidade',
        max_length=50,
        help_text = 'Ex: Barbacena',
        error_messages = {'required' : 'Por favor, insira a cidade', 'max_lenght' : 'A cidade é muito grande.'}
    )

    uf = models.CharField(
        verbose_name = 'UF',
        max_length=2,
        help_text = 'Ex: MG',
        error_messages = {'required' : 'Por favor, insira o UF', 'max_lenght' : 'Uma UF tem apenas 2 caracteres.'},
        validators=[ RegexValidator(r'^[A-Z][A-Z]$', message = 'Insira uma UF válida') ]
    )

    descricao = models.CharField(
        verbose_name = 'Descrição (Não obrigatório)',
        max_length = 300,
        help_text = 'Ex: Casa amarela localizada no fundo',
        error_messages = {'max_lenght' : 'O complemento é muito grande.'},
        blank = True
    )
    
    def __str__(self):
        return self.cep


class formEndereco(ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'descricao']
        widgets = {
            'cep' : forms.TextInput(attrs={'placeholder': 'Ex: 01001000'}),
            'endereco' : forms.TextInput(attrs={'placeholder': 'Ex: José Josino de Oliveira'}),
            'numero' : forms.TextInput(attrs={'placeholder': 'Ex: 83'}),
            'complemento' : forms.TextInput(attrs={'placeholder': 'Ex: D'}),            
            'bairro' : forms.TextInput(attrs={'placeholder': 'Ex: Funcionários '}),
            'cidade' : forms.TextInput(attrs={'placeholder': 'Ex: Barbacena'}),
            'uf' : forms.TextInput(attrs={'placeholder': 'Ex: MG'}),
            'descricao' : forms.TextInput(attrs={'placeholder': 'Ex: Casa amarela dos fundos'})
            }
#Criação do formulário com base do models do banco de dados.

