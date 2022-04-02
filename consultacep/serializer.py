from rest_framework import serializers
from cadastro.models import Endereco

class enderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['cep', 'endereco', 'bairro', 'cidade', 'uf' ]