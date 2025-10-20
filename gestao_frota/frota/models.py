from django.db import models

class Carro(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano_fabricacao = models.IntegerField(null=True, blank=True)
    em_manatencao = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Isso ajuda a mostrar uma informação legível no painel de administração
        return f"({self.marca} {self.modelo} {self.placa})"
