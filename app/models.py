from django.db import models
import datetime

# таблица app_data
class Data(models.Model):
    grazhdanstvo = models.CharField(max_length=30)
    grazhdanstvo2 = models.CharField(max_length=30, default='USA')
    kratnost = models.CharField(max_length=30)
    familiya = models.CharField(max_length=30, default='firstname')
    imya = models.CharField(max_length=30, default='secondname')
    data_rozh = models.DateField(default=datetime.date.today)
    nomer_pass = models.IntegerField(default=1111111111)
    prin_organiz = models.CharField(default="",max_length=10000)
    dop_svedeniya = models.CharField(default="",max_length=10000)



