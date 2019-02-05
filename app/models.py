from django.db import models
import datetime
import openpyxl
import re
from pprint import pprint

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




class Xlsx:
    def __init__(self,fname):
        self.wb = openpyxl.Workbook()
        self.fname = 'data.xlsx'


    def open(self):
        try:
            self.wb = openpyxl.load_workbook(filename=self.fname)
        except:
            pass
        self.ws1 = self.wb.active


    def WriteCell(self,cell,d):
        self.ws1[cell]=d

    def Close(self):
        self.wb.save(filename=self.fname)


        #



