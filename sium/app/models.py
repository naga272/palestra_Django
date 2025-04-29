from django.db import models
# Create your models here.


class Utente(models.Model):
    RUOLI = [
        ("passeggero", "Passeggero"),
        ("guidatore", "Guidatore")
    ]

    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    email = models.EmailField()
    ruolo = models.CharField(max_length=20, choices=RUOLI)
