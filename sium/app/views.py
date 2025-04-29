from django.shortcuts import render

# Create your views here.
from .form import Utenza


def homepage(request):
    return render(request, "index.html", { })


def form(request):
    if request.method == "POST":
        form = Utenza(request.POST)
        if form.is_valid():
            form.save()  # <<<<<<<<
            return render(request, "accepted.html", {})
    else:
        form = Utenza()

    return render(request, "form.html", {"form": form})

