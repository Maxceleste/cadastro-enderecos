from django.shortcuts import render, redirect
from .models import formEndereco

# Create your views here.

def index(request):
    return render(request, 'index.html')


def form(request):
    if request.method == 'POST':
        cadastro = formEndereco(request.POST)

        if cadastro.is_valid():
            cadastro.save()
            return redirect('index')

    else:
        cadastro = formEndereco()
    return render(request, 'form.html', {'cadastro':cadastro} )