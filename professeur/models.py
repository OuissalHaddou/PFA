from django.db import models

# Create your models here.                           
class Professeur(models.Model):
    # teacher_id = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    department = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    years_of_experience = models.IntegerField()
