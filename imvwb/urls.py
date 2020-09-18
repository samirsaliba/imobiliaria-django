from django.urls import path
from . import views

app_name = 'imvwb'
urlpatterns = [
    path('', views.index, name='index'),
    path('casas/<int:casa_id>/', views.detail_casa, name='detail_casa'),
    path('apartamentos/<int:apto_id>/', views.detail_apartamento, name='detail_apto'),
    path('cadastro_casa/', views.cadastro_casa, name='cadastro_casa'),
    path('casas/', views.lista_casas, name='casas'),
    path('apartamentos/', views.lista_aptos, name='aptos'),
    path('contato', views.contato, name='contato'),
]

