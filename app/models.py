from django.db import models


# таблица app_data
class Data(models.Model):
    grazhdanstvo = models.CharField(max_length=30)
    kratnost = models.CharField(max_length=30)
