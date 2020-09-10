from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Casa, Apartamento

# Create your views here.

def index(request):
    casas = Casa.objects.all()
    aptos = Apartamento.objects.all()

    context = {
        'casas':casas,
        'aptos':aptos
    }
    return render(request, 'imvwb/index.html', context)

class DetailCasaView(generic.DetailView):
    model = Casa
    template_name = 'imvwb/detail_casa.html'
    context_object_name = 'casa'


class DetailAptoView(generic.DetailView):
    model = Apartamento
    template_name = 'imvwb/detail_apto.html'
    context_object_name = 'apto'