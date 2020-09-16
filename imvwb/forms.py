from django import forms
from .models import Bairro

max_small_integer = 32767
max_positive_integer = 2147483647

class CasaForm(forms.Form):
    num_quartos = forms.IntegerField(label='Número de quartos', max_value=10)
    num_salas_estar = forms.IntegerField(label='Número de salas de estar', max_value=10)
    num_salas_jantar = forms.IntegerField(label='Número de salas de jantar', max_value=10)
    area = forms.IntegerField(label='Área (em m²)', max_value=max_small_integer)
    num_vagas_garagem = forms.IntegerField(label='Número de vagas de garagem', max_value=10)
    possui_armario_embutido = forms.BooleanField(label='Possui armário embutido?')
    

    logradouro = forms.CharField(label='Rua', max_length=100)
    numero = forms.CharField(label='Número', max_length=max_small_integer)
    bairro = forms.ModelChoiceField(label='Bairro', queryset=Bairro.objects.all())
    uf = forms.CharField(label='Unidade Federativa', max_length=2)
    cidade = forms.CharField(label='Cidade')
    aluguel = forms.IntegerField(label='Valor do aluguel', max_value=max_positive_integer)
    descricao = forms.CharField(label='Descricao', max_length=500)

    imagens = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    '''
    TODO: adicionar várias imagens juntas
    ver documentação - File Uploads https://docs.djangoproject.com/en/3.1/topics/http/file-uploads/
    detalhe para subseção - Uploading Multiple Files

    '''


class ApartamentoForm(forms.Form):
    num_quartos = forms.IntegerField(label='Número de quartos', max_value=10)
    num_salas_estar = forms.IntegerField(label='Número de salas de estar', max_value=10)
    num_salas_jantar = forms.IntegerField(label='Número de salas de jantar', max_value=10)
    area = forms.IntegerField(label='Área (em m²)', max_value=max_small_integer)
    num_vagas_garagem = forms.IntegerField(label='Número de vagas de garagem', max_value=10)
    possui_armario_embutido = forms.BooleanField(label='Possui armário embutido?')

    andar = forms.IntegerField(label='Andar', max_value=100)
    valor_condominio = forms.IntegerField(label='Valor do condomínio', max_value=PositiveSmallIntegerField)
    possui_portaria_24h = forms.BooleanField(label='Possui portaria 24hrs?')

    logradouro = forms.CharField(label='Rua', max_length=100)
    numero = forms.CharField(label='Número', max_length=max_small_integer)
    bairro = forms.ModelChoiceField(label='Bairro', queryset=Bairro.objects.all())
    uf = forms.CharField(label='Unidade Federativa', max_length=2)
    cidade = forms.CharField(label='Cidade')
    aluguel = forms.IntegerField(label='Valor do aluguel', max_value=max_positive_integer)
    descricao = forms.CharField(label='Descricao', max_length=500)