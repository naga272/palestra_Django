from django import forms
from .models import Persona


class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ["cod_fiscale", "nome", "cognome", "eta", "email"]
    