from django.db import models
import datetime
import re

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
    placement = models.TextField()
    rout = models.TextField()
    hostorganization = models.TextField()
    def __str__(self):
        return self.familyname

class Form2(models.Model):
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
    placement = models.TextField()
    rout = models.TextField()
    hostorganization = models.TextField()

    def __str__(self):
        return self.familyname

class GroupMembers(models.Model):
    form2 = models.ForeignKey(Form2,on_delete=models.CASCADE)
    familyname = models.CharField(max_length=30,default='')
    firstname = models.CharField(max_length=30,default='')
    name = models.CharField(max_length=30,default='')
    lastname = models.CharField(max_length=30,default='')
    birthday = models.DateField(default='')
    passport = models.TextField(default='')
    nationality = models.TextField(default='')

    def __str__(self):
        return self.familyname



#https://djbook.ru/rel1.6/topics/forms/modelforms.html

