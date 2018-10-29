from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from .models import Mascota

# Create your views here.


def mascota(request):
    mascotas = Mascota.objects.all()
    return render(request, "mascota/mascota.html", {'mascotas':mascotas})

def PageUpdate(UpdateView):
    model = Mascota
    fields =['title','raza','Estado','description','image'] 
    template_name_suffix ='_update_form'   





  