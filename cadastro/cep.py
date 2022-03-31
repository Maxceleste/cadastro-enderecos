import requests as re

def checar_cep(value):
    if len(value) == 8:
        cep = re.get(f'viacep.com.br/ws/{value}/json/')
        informacoes = cep.json()
        
