from django.db import models
import datetime

import re
from pprint import pprint

# таблица app_data
class Form1(models.Model):
    familyname = models.CharField(max_length=30, default='familyname')
    firstname = models.CharField(max_length=30,default='firstname')
    name = models.CharField(max_length=30,default='name')
    lastname = models.CharField(max_length=30, default='lastname')
    sex = models.CharField(max_length=10,default='sex')
    goal = models.CharField(max_length=30,default='goal')
    birthday = models.DateField(default=datetime.date(2019,1,1))
    passport = models.IntegerField(default=1111111111)
    entry = models.DateField(default=datetime.date(2019,1,1))
    departure = models.DateField(default=datetime.date(2019,1,1))
    nationality = models.CharField(default='nationality',max_length=1000)
    multiplicity = models.CharField(default='multipliticy',max_length=1000)
    confirmation = models.CharField(default='confirmation',max_length=1000)
    date = models.DateField(default=datetime.date(2019,1,1))
    placement = models.CharField(default="", max_length=10000)
    root = models.CharField(default="", max_length=10000)
    hostorganization = models.CharField(default="", max_length=10000)





