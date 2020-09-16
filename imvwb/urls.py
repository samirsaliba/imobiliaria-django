from django.urls import path
from . import views

app_name = 'imvwb'
urlpatterns = [
    path('', views.index, name='index'),
    path('casas/<int:casa_id>/', views.detail_casa, name='detail_casa'),
    path('aptos/<int:apto_id>/', views.detail_apartamento, name='detail_apto'),
    #path('cadastro_casa/', views.CadastroCasa.as_view(), name='cadastro_casa'),
    path('cadastro_casa/', views.cadastro_casa, name='cadastro_casa'),

]

