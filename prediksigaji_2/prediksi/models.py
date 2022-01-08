from django.db import models
from django.forms import ModelForm, Textarea

# Create your models here.

class Pegawai(models.Model):
    Age = models.FloatField()
    JobLevel = models.IntegerField()
    MonthlyIncome = models.IntegerField()
    TotalWorkingYears = models.IntegerField()
    YearsAtCompany = models.IntegerField()


class Meta:
    db_table = "pegawai"
