from django.db import models


# таблица app_data
class Data(models.Model):
    # name = models.CharField(max_length=21)
    # age = models.IntegerField()
    grazhdanstvo = models.CharField(max_length=30)
    kratnost = models.CharField(max_length=30)
