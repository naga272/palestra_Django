from django import forms
from .models import Utente


class Utenza(forms.ModelForm):
    class Meta:
        model = Utente
        fields = ['nome', 'cognome', 'email', 'ruolo']
