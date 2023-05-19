from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('professeur/', views.display_professeur, name='display_professeur'),
]