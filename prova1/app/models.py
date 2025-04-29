from django.db import models

# Create your models here.

class Persona(models.Model):
    cod_fiscale = models.CharField(max_length=200, primary_key=True)
    nome        = models.CharField(max_length=200)
    cognome     = models.CharField(max_length=200)
    eta         = models.CharField(max_length=20)
    email       = models.EmailField()
