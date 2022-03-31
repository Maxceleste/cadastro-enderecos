from django.contrib import admin
from .models import Endereco

class DisplayEnderecos(admin.ModelAdmin):
    list_display = ('cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'descricao')
    search_fields = ('cep',)
    list_filter = ('uf',)
    list_per_page = 10


admin.site.register(Endereco, DisplayEnderecos)
