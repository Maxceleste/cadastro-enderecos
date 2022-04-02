from rest_framework import viewsets
from cadastro.models import Endereco
from serializer import enderecoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    """ Testando e exibindo todos os ceps """
    queryset = Endereco.objects.all()
    serializer_class = enderecoSerializer
