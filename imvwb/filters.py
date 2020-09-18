from django.contrib.auth.models import User
from .models import Imovel, Casa, Apartamento, Bairro
from django import forms
from django.db import models
import django_filters

# Referencia dos filtros
# https://docs.djangoproject.com/en/3.1/topics/forms/#rendering-fields-manually
# Para as classes, campos https://django-filter.readthedocs.io/en/stable/index.html
# Para os widgets:
# https://docs.djangoproject.com/en/3.1/ref/forms/widgets/
# e https://getbootstrap.com/docs/4.0/components/forms/

class ApartamentoFilter(django_filters.FilterSet):
    aluguel__lt = django_filters.NumberFilter(field_name='aluguel', lookup_expr='lt', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    aluguel__gt = django_filters.NumberFilter(field_name='aluguel', lookup_expr='gt', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    possui_portaria_24h = django_filters.BooleanFilter(field_name='possui_portaria_24h')
    bairro = django_filters.ModelChoiceFilter(queryset=Bairro.objects.all(), widget=forms.Select(attrs={'class': 'custom-select'}))
    quartos__gt = django_filters.NumberFilter(field_name='num_quartos', lookup_expr='gt', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Apartamento
        fields = ['aluguel__gt', 'aluguel__lt', 'possui_portaria_24h', 'quartos__gt', 'bairro']

