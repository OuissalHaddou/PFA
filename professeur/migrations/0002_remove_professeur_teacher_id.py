# Generated by Django 4.1.7 on 2023-05-18 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professeur', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professeur',
            name='teacher_id',
        ),
    ]
