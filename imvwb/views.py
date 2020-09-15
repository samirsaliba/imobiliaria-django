from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Casa, Apartamento, Imagem

# Create your views here.

def index(request):
    casas = Casa.objects.order_by('data_postagem')[:5]
    aptos = Apartamento.objects.order_by('data_postagem')[:5]

    context = {
        'casas':casas,
        'aptos':aptos
    }
    return render(request, 'imvwb/index.html', context)

def detail_casa(request, casa_id):
    casa = get_object_or_404(Casa, pk=casa_id)
    imagens = Imagem.objects.filter(imovel=casa_id)
    context = {'casa': casa, 'imagens': imagens}

    return render(request, 'imvwb/detail_casa.html', context)

def detail_apartamento(request, apto_id):
    apto = get_object_or_404(Apartamento, pk=apto_id)
    imagens = Imagem.objects.filter(imovel=apto_id)
    context = {'apto': apto, 'imagens': imagens}

    return render(request, 'imvwb/detail_apto.html', context)
