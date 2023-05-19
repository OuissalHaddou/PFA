from django.urls import path
from . import views

urlpatterns = [
    path('<int:etudiant_id>/etudiant', views.etudiant_detail, name='etudiant_detail'),
]