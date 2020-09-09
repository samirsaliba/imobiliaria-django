from django.urls import path

from . import views
app_name = 'imvwb'
urlpatterns = [
    path('', views.index, name='index'),
    path('casas/<int:casa_id>/', views.detail_casa, name='detail_casa'),
    path('aptos/<int:apto_id>/', views.detail_apto, name='detail_apto'),
]