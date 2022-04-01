from doctest import testfile
from django.shortcuts import render, redirect
from .models import formEndereco, Endereco

# Create your views here.

def index(request):

    enderecos = Endereco.objects.all() 
    #Pegando todos os endereços do banco

    dados = {
        'enderecos' : enderecos
    }
    #Inserindo nos dados os endereços

    return render(request, 'index.html', dados)
    #Retornando na página o HTML e os dados


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
    #Se a página der request de POST, irá pegar todos os posts dos campos. (Coloquei "1" no final para diferenciar)
        
        

        if cadastro.is_valid():  
            if Endereco.objects.filter(cep=cep1, endereco = endereco1, bairro = bairro1, cidade = cidade1, uf = uf1, numero=numero1):
                endereco_anterior = Endereco.objects.get(cep=cep1, endereco = endereco1, bairro = bairro1, cidade = cidade1, uf = uf1, numero=numero1)
                endereco_anterior.complemento = complemento1
                endereco_anterior.descricao = descricao1
                endereco_anterior.save()
            #Se o cadastro estiver tudo validado, irá checar se os campos obrigatórios ja foram inseridos.
            #Caso já forma inseridos, ele apenas irá atualizar o já cadastrado com os campos não obrigatórios.
            else:
                cadastro.save()
            #Caso os campos obrigatórios sejam novos, ele vai salvar um novo endereço no banco.        
            return redirect('index')
            #E assim, depois desse processo ele te redireciona para a página index
    else:
    #Esse else representa "caso o método post não seja chamado", ou seja, o método GET
        cadastro = formEndereco()
    #Aqui ele determina o cadastro como o model form que fizemos

    dados = {
        'cadastro' : cadastro,
    }
    #Adiciona o cadastro nos dados, e envia para o site para renderizar tudo.
    return render(request, 'form.html', dados )