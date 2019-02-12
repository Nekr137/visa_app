from django.db import models
import datetime
from .Xlsx import Xlsx
import openpyxl,re
from django.http import HttpResponseRedirect,HttpResponse, FileResponse
from openpyxl.writer.excel import save_virtual_workbook

def date_format(d):
    d = re.findall(r'\d+', str(d))
    d.reverse()
    return '.'.join(d)


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

    P = ['Фамилия', 'First name', 'Имя, Отчество', 'Last name', 'Пол', 'Цель поездки',
    'Дата рождения', 'Номер паспорта', 'Въезд с', 'Выезд до', 'Гражданство', 'Кратность визы',
    'Подтверждение №', 'Дата документа', 'Размещение', 'Маршрушт', 'Принимающая организация']

    def __str__(self):
        return self.familyname

    def GenerateXlsx(self,fin,fout):
        self.fname = fin
        self.wb = openpyxl.Workbook()
        self.wb = openpyxl.load_workbook(filename=self.fname)

        sheet1 = self.wb.get_sheet_by_name("Лист1")
        sheet1['F2'] = self.confirmation
        sheet1['D5'] = self.multiplicity
        sheet1['D7'] = self.nationality
        sheet1['C9'] = self.entry
        sheet1['F9'] = self.departure
        sheet1['C11'] = str(self.lastname) + '/' + str(self.familyname)
        sheet1['E13'] = str(self.firstname) + '/' + str(self.name)
        sheet1['D15'] = date_format(self.birthday)
        sheet1['G15'] = self.sex
        sheet1['D17'] = self.passport
        sheet1['D19'] = self.goal
        sheet1['D40'] = self.date
        sheet1['M40'] = self.date

        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename='+fout
        self.wb.save(response)
        return response



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
        return 'Familyname: ' + self.familyname + ' Name: ' + self.name + ' '


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

