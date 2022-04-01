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
        if cadastro.is_valid():   
                

            cadastro.save()
            return redirect('index')


    else:
        cadastro = formEndereco()

    dados = {
        'cadastro':cadastro
    }
    return render(request, 'form.html', dados )