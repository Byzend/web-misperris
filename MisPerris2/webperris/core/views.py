from django.shortcuts import render, HttpResponse



# Create your views here.
def form(request): 
    return render(request, "core/form.html")

def base(request):
    return render(request, "core/base.html")



