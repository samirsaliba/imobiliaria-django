from django.db import models

# Create your models here.
class Bairro(models.Model):
    nome = models.CharField(max_length=30, blank=False)
    def __str__(self):
        return self.nome

class Imovel(models.Model):
    '''
    quantidade de quartos, quantidade de suítes, quantidade de salas de estar, 
    número de vagas na garagem, área (em metros quadrados), 
    se possui armário embutido e descrição
    '''
    num_quartos = models.PositiveSmallIntegerField(blank=False)
    num_salas_estar = models.PositiveSmallIntegerField(blank=False)
    num_salas_jantar = models.PositiveSmallIntegerField(blank=False)
    area = models.PositiveSmallIntegerField(blank=False)
    num_vagas_garagem = models.PositiveSmallIntegerField(blank=False)
    possui_armario_embutido = models.BooleanField(default=None)
    descricao = models.TextField(max_length=500, blank=True)
    aluguel = models.PositiveIntegerField(blank=False)
    
    logradouro = models.CharField(max_length=50, blank=False)
    numero = models.PositiveSmallIntegerField(blank=False)
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT)
    cidade = models.CharField(max_length=25, blank=False)
    uf = models.CharField(max_length=2, blank=False)

    class Meta:
        abstract = True

class Casa(Imovel):
    def __str__(self):
        return "{} nº {}, {}, {}, {}".format(self.logradouro, self.numero, self.bairro, self.cidade, self.uf)

    pass

class Apartamento(Imovel):
    andar = models.PositiveSmallIntegerField(blank=False)
    valor_condominio = models.PositiveSmallIntegerField(blank=False)
    possui_portaria_24h = models.BooleanField(default=None)

    def __str__(self):
        return "{} nº {}, {}º andar, {}, {}, {}".format(self.logradouro, self.numero, self.andar, self.bairro, self.cidade, self.uf)

