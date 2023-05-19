from django.db import models

# Create your models here.
class Etudiant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    department = models.CharField(max_length=255)
    absence = models.IntegerField()
    justifier = models.IntegerField()
    non_justifier = models.IntegerField()
    justification = models.CharField(max_length=255)
