from django.http import JsonResponse 

def consultar_cep(request):
    if request.method == 'GET':
        cep = {'cep' : '75706835'}
        return JsonResponse(cep)
