from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'imvwb'
urlpatterns = [
    path('', views.index, name='index'),
    path('casas/<int:casa_id>/', views.detail_casa, name='detail_casa'),
    path('apartamentos/<int:apto_id>/', views.detail_apto, name='detail_apto'),
    path('cadastro_casa/', views.cadastro_casa, name='cadastro_casa'),
    path('cadastro_apartamento/', views.cadastro_apto, name='cadastro_apto'),
    path('casas/', views.lista_casas, name='casas'),
    path('apartamentos/', views.lista_aptos, name='aptos'),
    path('contato', views.contato, name='contato'),
    path('entrar/', auth_views.LoginView.as_view(template_name='imvwb/entrar.html'), name='entrar')
]

