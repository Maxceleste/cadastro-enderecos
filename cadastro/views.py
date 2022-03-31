from django.shortcuts import render, redirect
from .forms import CadastroEnderecos

# Create your views here.

def index(request):
    return render(request, 'index.html')


def form(request):
    if request.method == 'POST':
        cadastro = CadastroEnderecos(request.POST)

        if cadastro.is_valid():
            return redirect('index')

    else:
        cadastro = CadastroEnderecos()
    return render(request, 'form.html', {'cadastro':cadastro} )