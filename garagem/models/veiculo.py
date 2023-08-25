from django.db import models

class Veiculo(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome

