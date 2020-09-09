from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Casa, Apartamento, Imovel

# Create your views here.

def index(request):
    casas = Casa.objects.all()
    aptos = Apartamento.objects.all()

    context = {
        'casas':casas,
        'aptos':aptos
    }
    return render(request, 'imvwb/index.html', context)

def detail_casa(request, casa_id):
   
    casa = get_object_or_404(Casa, pk=casa_id)
    context = {'casa': casa}

    return render(request, 'imvwb/detail_casa.html', context)

def detail_apto(request, apto_id):
    
    apto = get_object_or_404(Apartamento, pk=apto_id)
    context = {'apto': apto}
    
    return render(request, 'imvwb/detail_apto.html', context)