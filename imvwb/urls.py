from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'imvwb'
urlpatterns = [
    path('', views.index, name='index'),
    path('casas/<int:casa_id>/', views.detail_casa, name='detail_casa'),
    path('aptos/<int:apto_id>/', views.detail_apartamento, name='detail_apto'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
