from django.shortcuts import render

from .models import *

#from .forms import *


def index(request):
    return render(request,'professeur/index.html')

def display_professeur(request):
    items = Professeur.objects.all()
    context = {
        'items': items,
        'header': 'Professeur',
    }
    return render(request,'professeur/index.html', context)