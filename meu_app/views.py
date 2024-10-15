from django.shortcuts import render

from .models import Pets



# Create your views here.
from django.shortcuts import render

def home(request):
    pets = Pets.objects.all()
    return render(request, 'home.html', {'pets': pets})
