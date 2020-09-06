from django.contrib import admin
from .models import Apartamento, Casa, Bairro

# Register your models here.
admin.site.register(Apartamento)
admin.site.register(Casa)
admin.site.register(Bairro)