from django import forms
from django.core.validators import RegexValidator

class CadastroEnderecos(forms.Form):
    cep = forms.CharField(label = "CEP",
    max_length = 8 ,
    help_text='Ex: 30190906',
    validators=[ RegexValidator(r'^\d\d\d\d\d\d\d\d$', message = 'Insira um CEP válido')  ], 
    error_messages = {'required' : 'Por favor, insira o CEP', 'max_lenght' : 'O CEP deve conter 8 números.' }
    )