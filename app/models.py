from django.db import models
import datetime
import re
from pprint import pprint

# таблица app_data
class Form1(models.Model):
    familyname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    goal = models.CharField(max_length=30)
    birthday = models.DateField()
    passport = models.TextField()
    entry = models.DateField()
    departure = models.DateField()
    nationality = models.TextField()
    multiplicity = models.TextField()
    confirmation = models.TextField()
    date = models.DateField()
    type = models.TextField()
    type2 = models.TextField()
    # placement = models.TextField()
    # rout = models.TextField()
    # hostorganization = models.TextField()




#https://djbook.ru/rel1.6/topics/forms/modelforms.html

