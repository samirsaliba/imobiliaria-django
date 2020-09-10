from django.urls import path
from . import views

app_name = 'imvwb'
urlpatterns = [
    path('', views.index, name='index'),
    path('casas/<int:pk>/', views.DetailCasaView.as_view(), name='detail_casa'),
    path('aptos/<int:pk>/', views.DetailAptoView.as_view(), name='detail_apto'),
]