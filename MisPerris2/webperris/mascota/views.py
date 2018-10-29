from django.shortcuts import render
from .models import Mascota

# Create your views here.


def mascota(request):
    mascotas = Mascota.objects.all()
    return render(request, "mascota/mascota.html", {'mascotas':mascotas})