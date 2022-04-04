# Cadastro de endereços
![APM](https://img.shields.io/apm/l/vim-mode)

Um app web fullstack construído com Django, onde se cadastra endereços em um banco de dados, com um preenchimento automático do cep.

# Instalação
A primeira coisa que você deve fazer é instalar a venv na pasta e depois entrar na venv.

Assim, abra o arquivo `requirements.txt` e instale tudo que contém nesse arquivo com o pip.

Crie um banco de dados Mysql com o nome que queira.

Perceba que foi instalado o python decouple também. Crie na raiz do repositório um arquivo chamado `.env` e dentro dele coloque as seguintes chaves:

![image](https://user-images.githubusercontent.com/89614438/161355350-db4974cd-23b4-4a8c-89be-c925c01b0751.png)

Agora, execute as migrações do django com:

```
python manage.py makemigrations

```

```
python manage.py migrate

```

Caso queira usar o Django admin, terá que criar um superuser com o comando:

```
python manage.py createsuperuser

```

Assim que criar, pode logar no django admin tranquilamente.

Após isso, pode testar executando no terminal:
```
python manage.py runserver

```
E aproveite!

## Funcionalidades

- Duas telas, uma de listagem de endereços, e a outra de cadastrar os endereços.
- Opçao de cadastrar endereço, com todos os campos necessários.
- Preenchimento automático dos campos por meio do cep, consumindo a api Viacep com JQuery.
- Quando se tenta cadastrar um endereço com os valores obrigatórios de outro endereço existente, altera os valores não obrigatórios anteriores com novos valores
- Django Admin configurado e fácil de usar para alteração de endereços inseridos.
- Uso do banco de dados MySQL

## Visão do site


### Página de listagem de endereços sem nenhum endereço inserido

![image](https://user-images.githubusercontent.com/89614438/161352320-8e87cc3a-218e-4d24-9ee0-1d7ddd0f7703.png)


### Página de listagem de endereços com endereços inseridos

![image](https://user-images.githubusercontent.com/89614438/161352867-1bc2e984-9876-4007-ae42-abd6e44d0d83.png)


### Página de cadastro de endereços

![image](https://user-images.githubusercontent.com/89614438/161352424-3342feb0-7c7a-4fad-98f2-299f32ccaba6.png)

### Django admin

![image](https://user-images.githubusercontent.com/89614438/161352898-2539ad23-1a7b-4c4b-abb9-65d813077a0f.png)

O Frontend desse projeto não é o foco, mas são páginas que funcionam mesmo não sendo tão bonitas.

## Como funciona?

Nesse projeto simples, utilizei o banco de dados como base para fazer o formulário, ou seja, utilizei a API do django ModelForm.
Observer o campo CEP por exemplo:

![image](https://user-images.githubusercontent.com/89614438/161353106-714decba-a3d8-4a1c-b570-f6e3a41cd9c1.png)

Perceba que ele ja é todo configurado para poder se transformar em um bom Forms, além de que usa o Regex validator para que seja inserido o cep de forma correta, tanto no forms quanto no Django admin. Todos os campos seguem esse padrão.

Além disso, nas view da parte de cadastro há algumas funcionalidades:

![image](https://user-images.githubusercontent.com/89614438/161353301-26887fe7-1511-4054-8adb-cf088f7b48b5.png)

Nese trecho da view, o programa checa se todos os valores obrigatórios já existem na tabela, assim, apenas alterando o campo existente com os valores não obrigatórios.
Caso sejam valores novos, apenas irá gravar na tabela um novo endereço.

![image](https://user-images.githubusercontent.com/89614438/161353994-3a74cfce-59da-4b2e-b487-d376ac5458c1.png)

Observe na imagem aciama, o código em Javascript utilizando JQuery.
Quando se tira o foco do campo de cep, é ativado esse evento onde:
- Ele tenta fazer a request da api de cep
- Se der certo, ele preenche os espaços com "..." até o valor aparecerem
- Caso a api devolva erro, os campos vão ficar vazios de novo e o evento vai acabar.
- Caso a api devolva o resultado correto, os valores aparecem no campo desejado e assim o foco muda para o próximo campo vazio.

![image](https://user-images.githubusercontent.com/89614438/161354120-9e350883-2196-4126-9a98-c297d1b5b51a.png)

Na imagem acima, perceba que todo o forms foi colocado manualmente. Fiz assim para uma melhor formataçao e estilização.

Na imagem abaixo está o HTML do index, onde também estão os códigos python:

![image](https://user-images.githubusercontent.com/89614438/161354216-4aea4a3f-6101-4643-aac7-cc46fd04e87a.png)

Esse é o código da tabela. Perceba que a primeira coisa que é realizada é um teste para saber se há endereços cadastrados. Caso não haja, apenas será mostrado que não há endereços na tela.
Caso haja, ele faz um loop por todo o conteúdo do banco e mostra pro usuário em forma de tabela.

# Autor

Nome: Max Paulo Simão Teixeira

Linkedin: https://www.linkedin.com/in/max-paulo-sim%C3%A3o-teixeira-278a4a212



