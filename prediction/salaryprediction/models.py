from django.forms import ModelForm, Textarea
from django.db import models

# Create your models here.
class Pegawai(models.Model):
    id = models.IntegerField()
    YearsExperience = models.FloatField(max_length=11)
    Salary = models.IntegerField()
class Meta :
    db_table = 'gaji'