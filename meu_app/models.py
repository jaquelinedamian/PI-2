from django.db import models
# Lista
TIPOS_PETS = {
    "DOG": "Cachorro",
    "CAT": "Gato"
}

# Modelo de banco de dados.
class Pets(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=3, choices=TIPOS_PETS.items())
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
