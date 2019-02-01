from django.db import models


# таблица app_data
class Data(models.Model):
    grazhdanstvo = models.CharField(max_length=30)
    kratnost = models.CharField(max_length=30)

    familiya = models.CharField(max_length=30)
    imya = models.CharField(max_length=30)
    data_rozh = models.CharField(max_length=30)
    nomer_pass = models.IntegerField()
    grazhdanstvo2 = models.CharField(max_length=30)