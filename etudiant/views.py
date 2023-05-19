from django.shortcuts import render
from .models import Etudiant

def etudiant_detail(request, etudiant_id):
    etudiant = Etudiant.objects.get(id=etudiant_id)
    return render(request,'etudiant/home.html',{'etudiant': etudiant})