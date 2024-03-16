from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == "POST":
        numero1 = float(request.POST.get('numero1', 0))
        numero2 = float(request.POST.get('numero2', 0))
    return render(request, 'home/index.html')


def calcular(request): 
    pass
    