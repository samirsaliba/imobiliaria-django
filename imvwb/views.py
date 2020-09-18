from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import datetime
from django.utils import timezone

from .models import Imovel, Casa, Apartamento, Imagem
from .forms import CasaForm, ApartamentoForm
from .filters import ApartamentoFilter


# Create your views here.

def index(request):
    casas = Casa.objects.order_by('data_postagem')[:5]
    aptos = Apartamento.objects.order_by('data_postagem')[:5]

    now = timezone.now()
    one_week_ago = now-datetime.timedelta(7)

    for casa in casas:
        imagem = Imagem.objects.filter(imovel_id=casa.id)[0]
        casa.imagem = imagem.imagem
        casa.new=True if casa.data_postagem > one_week_ago else False


    for apto in aptos:
        imagem = Imagem.objects.filter(imovel_id=apto.id)[0]
        apto.imagem = imagem.imagem
        apto.new=True if casa.data_postagem > one_week_ago else False

    context = {
        'casas':casas,
        'aptos':aptos
    }
    return render(request, 'imvwb/index.html', context)

def contato(request):
    context = {}
    return render(request, 'imvwb/contato.html', context)

def detail_casa(request, casa_id):
    casa = get_object_or_404(Casa, pk=casa_id)
    imagens = Imagem.objects.filter(imovel=casa_id)

    print(imagens)
    context = {'casa': casa, 'imagens': imagens}

    return render(request, 'imvwb/detail_casa.html', context)

def detail_apartamento(request, apto_id):
    apto = get_object_or_404(Apartamento, pk=apto_id)
    imagens = Imagem.objects.filter(imovel=apto_id)
    context = {'apto': apto, 'imagens': imagens}

    return render(request, 'imvwb/detail_apto.html', context)

def cadastro_casa(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CasaForm(request.POST, request.FILES)
        # check whether it's valid:

        if form.is_valid():
            # Se o form for valido, cadastrar a Casa
            num_quartos = form.cleaned_data['num_quartos']
            num_salas_estar = form.cleaned_data['num_salas_estar']
            num_salas_jantar = form.cleaned_data['num_salas_jantar']
            area = form.cleaned_data['area']
            num_vagas_garagem = form.cleaned_data['num_vagas_garagem']
            possui_armario_embutido = form.cleaned_data['possui_armario_embutido']
            
            logradouro = form.cleaned_data['logradouro']
            numero = form.cleaned_data['numero']
            bairro = form.cleaned_data['bairro']
            uf = form.cleaned_data['uf']
            cidade = form.cleaned_data['cidade']
            aluguel = form.cleaned_data['aluguel']
            descricao = form.cleaned_data['descricao']

            casa = Casa(
                num_quartos = num_quartos,
                num_salas_estar = num_salas_estar,
                num_salas_jantar = num_salas_jantar,
                area = area,
                num_vagas_garagem = num_vagas_garagem,
                possui_armario_embutido = possui_armario_embutido,
                descricao = descricao,
                aluguel = aluguel,
                logradouro = logradouro,
                numero = numero,
                bairro = bairro,
                cidade = cidade,
                uf = uf,
            )

            casa.save()
            files = request.FILES.getlist('imagens')
            imovel = Imovel.objects.get(pk=casa.id)

            for img in files:
                # Apos ter criado a casa, cadastrar cada imagem - com a PK da casa
                
                img_objeto = Imagem(
                        imagem = img,
                        imovel = imovel
                )
                img_objeto.save()
            
            return HttpResponseRedirect(reverse('imvwb:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CasaForm()

    return render(request, 'imvwb/cadastro_imovel.html', {'form': form})

def lista_casas(request):
    casas = Casa.objects.order_by('data_postagem')
    now = timezone.now()
    one_week_ago = now-datetime.timedelta(7)

    for casa in casas:
        imagem = Imagem.objects.filter(imovel_id=casa.id)[0]
        casa.imagem = imagem.imagem
        casa.new=True if casa.data_postagem > one_week_ago else False
    
    context = {
        'casas':casas,
    }
    return render(request, 'imvwb/lista_casas.html', context)

def lista_aptos(request):
    aptos_list = Apartamento.objects.order_by('data_postagem')
    apto_filter = ApartamentoFilter(request.GET, queryset=aptos_list)

    now = timezone.now()
    one_week_ago = now-datetime.timedelta(7)

    for apto in apto_filter.qs:
        imagem = Imagem.objects.filter(imovel_id=apto.id)[0]
        apto.imagem = imagem.imagem
        apto.new=True if apto.data_postagem > one_week_ago else False
    
    context = {
        'aptos':apto_filter.qs,
        'form':apto_filter.form
    }

    return render(request, 'imvwb/lista_aptos.html', context)
