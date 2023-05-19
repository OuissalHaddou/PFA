from django.urls import path
from . import views

urlpatterns = [
    path('etudiant/<int:etudiant_id>/', views.etudiant_detail, name='etudiant_detail'),
]