from doctest import testfile
from django.shortcuts import render, redirect
from .models import formEndereco, Endereco

# Create your views here.

def index(request):

    enderecos = Endereco.objects.all()

    dados = {
        'enderecos' : enderecos
    }

    return render(request, 'index.html', dados)


def form(request):

    if request.method == 'POST':
        cadastro = formEndereco(request.POST)
        cep1 = request.POST['cep']
        endereco1 = request.POST['endereco']
        bairro1 = request.POST['bairro']
        numero1 = request.POST['numero']
        cidade1 = request.POST['cidade']
        uf1 = request.POST['uf']
        complemento1 = request.POST['complemento']
        descricao1 = request.POST['descricao']

        
        

        if cadastro.is_valid():  
            if Endereco.objects.filter(cep=cep1, endereco = endereco1, bairro = bairro1, cidade = cidade1, uf = uf1, numero=numero1):
                endereco_anterior = Endereco.objects.get(cep=cep1, endereco = endereco1, bairro = bairro1, cidade = cidade1, uf = uf1, numero=numero1)
                endereco_anterior.complemento = complemento1
                endereco_anterior.descricao = descricao1
                endereco_anterior.save()
            else:
                cadastro.save()        
            return redirect('index')


    else:
        cadastro = formEndereco()

    dados = {
        'cadastro' : cadastro,
    }
    return render(request, 'form.html', dados )