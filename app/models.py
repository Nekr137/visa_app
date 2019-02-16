from django.db import models
import datetime
import openpyxl,re
from django.http import HttpResponseRedirect,HttpResponse, FileResponse
from openpyxl.writer.excel import save_virtual_workbook
from django.forms import ModelChoiceField

def date_format(d):
    """Дата в формате dd.mm.yyyy"""
    d = re.findall(r'\d+', str(d))
    d.reverse()
    return '.'.join(d)

def SplitRout(r):
    """Разбивает поле маршрут так, чтобы текст равномерно разместился в двух ячейках"""
    return r[:25],r[25:]


def SplitOrganization(o):
    """Разбивает поле организации так, чтобы текст равномерно разместился в двух ячейках"""
    return o[:50],o[50:]

def SplitInfo(i):
    """Разбивает поле дополнительная информация на 4 ячейки"""
    return i[0:25],i[25:75],i[75:125],i[125:175]


class AdditionalInfo(models.Model):
    info = models.TextField()
    default = models.BooleanField(default=False)
    def __str__(self):
        return self.info

class Placements(models.Model):
    placement = models.TextField()
    default = models.BooleanField(default=False)
    def __str__(self):
        return self.placement

class Organizations(models.Model):
    organization = models.TextField()
    default = models.BooleanField(default=False)
    def __str__(self):
        return self.organization

class Nationality(models.Model):
    nationality = models.CharField(max_length=100)
    default = models.BooleanField(default=False)
    def __str__(self):
        return self.nationality


class Routs(models.Model):
    rout = models.TextField()
    default = models.BooleanField(default=False)
    def __str__(self):
        return self.rout

class Ships(models.Model):
    name = models.CharField(max_length=30)
    default = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Dates(models.Model):
    ship = models.ForeignKey(Ships, on_delete=models.CASCADE)
    entry = models.DateField()
    departure = models.DateField()
    default = models.BooleanField(default=False)
    def __str__(self):
        return str(self.entry) + '/' + str(self.departure)


class Form1(models.Model):
    familyname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    goal = models.CharField(max_length=30)
    birthday = models.DateField()
    passport = models.TextField()
    multiplicity = models.TextField()
    date = models.DateField()
    confirmation = models.TextField()
    nationality = models.TextField()
    entry = models.DateField()
    departure = models.DateField()
    placement = models.TextField()
    rout = models.TextField()
    hostorganization = models.TextField()
    additionalinfo = models.TextField()

    P = ['Фамилия', 'First name', 'Имя, Отчество', 'Last name', 'Пол', 'Цель поездки',
    'Дата рождения', 'Номер паспорта', 'Въезд с', 'Выезд до', 'Гражданство', 'Кратность визы',
    'Подтверждение №', 'Дата документа', 'Размещение', 'Маршрушт', 'Принимающая организация']

    def __str__(self):
        return self.familyname

    def GenerateXlsx(self,fin,fout):
        self.fname = fin
        #self.wb = openpyxl.Workbook()
        self.wb = openpyxl.load_workbook(filename=self.fname)

        sheet1 = self.wb["Лист1"]

        if self.confirmation:
            sheet1['F2'] = '0011 - AUS  06/07'
        sheet1['B5'] = 'визовое приглашение № 0047'
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
        sheet1['D24'] = self.placement
        sheet1['B26'],sheet1['B27'] = SplitOrganization(self.hostorganization)
        sheet1['F21'],sheet1['B22'] = SplitRout(self.rout)
        sheet1['E31'],sheet1['B32'],sheet1['B33'],sheet1['B34'] = SplitInfo(self.additionalinfo)

        img = openpyxl.drawing.image.Image('static/xlsx/pe.png')
        #img.anchor(sheet1.cell('A33'))
        img.anchor(sheet1.cell('F28'))
        sheet1.add_image(img)

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
    multiplicity = models.TextField()
    date = models.DateField()
    confirmation = models.TextField()
    nationality = models.TextField()
    entry = models.DateField()
    departure = models.DateField()
    placement = models.TextField()
    rout = models.TextField()
    hostorganization = models.TextField()
    additionalinfo = models.TextField()

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

