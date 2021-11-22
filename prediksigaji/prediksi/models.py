from django.db import models
from django.forms import ModelForm, Textarea

# Create your models here.


class Pegawai(models.Model):
    YearsExperience = models.FloatField()
    Salary = models.FloatField()


class Meta:
    db_table = "pegawai"
