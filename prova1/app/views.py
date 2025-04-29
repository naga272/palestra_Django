from django.shortcuts import render

# Create your views here.
from app.form import FormPersona


def homepage(request):
    return render(request, "index.html", {})


def form(request):
    if request.method == "POST":
        user = FormPersona(request.POST)
        if user.is_valid():
            print(user.cleaned_data["email"])
            user.save()

    context = {
        "persona" : FormPersona
    }
    return render(request, "form.html", context)


from app.models import Persona
def extraxt_users(request):
    users = Persona.objects.all() 
    return render(request, "all_users.html", {"users" : users})
