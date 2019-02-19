from django.db import models
import datetime
import openpyxl,re
from django.http import HttpResponseRedirect,HttpResponse, FileResponse
from openpyxl.writer.excel import save_virtual_workbook
from django.forms import ModelChoiceField
from transliterate import translit

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


class VisaNumber(models.Model):
    visanumber = models.IntegerField()
    def __str__(self):
        return str(self.visanumber)

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

    def __str__(self):
        return self.familyname

    def FormXlsx(self,fin):
        self.fname = fin
        self.wb = openpyxl.Workbook()
        self.wb = openpyxl.load_workbook(filename=self.fname)
        #sheet1 = self.wb["Лист1"]
        sheet1 = self.wb.active
        sheet1['F2'] = '0011 - AUS  06/07'
        sheet1['B5'] = 'визовое приглашение № 0047'
        sheet1['D7'] = self.multiplicity
        sheet1['D9'] = self.nationality
        sheet1['C11'] = self.entry
        sheet1['L11'] = self.entry
        sheet1['F11'] = self.departure
        sheet1['O11'] = self.departure
        sheet1['C13'] = str(self.familyname).upper() + '/' + str(self.firstname).upper()
        sheet1['E15'] = str(self.name).upper() + '/' + str(self.lastname).upper()
        sheet1['D17'] = date_format(self.birthday)
        sheet1['G17'] = str(self.sex).upper()
        sheet1['D19'] = self.passport
        sheet1['D21'] = str(self.goal).upper()
        #sheet1['D40'] = self.date
        #sheet1['M40'] = self.date
        sheet1['D25'] = self.placement
        sheet1['B27'],sheet1['B28'] = SplitOrganization(self.hostorganization)
        sheet1['F23'],sheet1['B24'] = SplitRout(self.rout)
        sheet1['E31'],sheet1['B32'],sheet1['B33'],sheet1['B34'] = SplitInfo(self.additionalinfo)

        pech = openpyxl.drawing.image.Image('static/xlsx/image823.png')
        pech2 = openpyxl.drawing.image.Image('static/xlsx/image823.png')
        pod = openpyxl.drawing.image.Image('static/xlsx/image853.png')
        pod2 = openpyxl.drawing.image.Image('static/xlsx/image853.png')
        sheet1.add_image(pech, 'A34')
        sheet1.add_image(pech2,'K34')
        sheet1.add_image(pod, 'C34')
        sheet1.add_image(pod2,'M34')


    def GenerateXlsx(self,fout):
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename='+fout
        self.wb.save(response)
        #self.wb.save(filename='test.xlsx')
        return response

    def GeneratePdf(self,fout):
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
        return 'Familyname: ' + self.familyname + ' Name: ' + self.name


    def FormXlsx(self,fin):
        self.fname = fin
        self.wb = openpyxl.Workbook()
        self.wb = openpyxl.load_workbook(filename=self.fname)

        #sheet1 = self.wb["Лист1"]
        sheet1 = self.wb.active
        sheet1['F2'] = '0011 - AUS  06/07'
        sheet1['B6'] = 'визовое приглашение № 0307'
        sheet1['K6'] = 'визовое приглашение № 0307'
        sheet1['D8'] = self.multiplicity
        sheet1['H16'] = self.nationality
        sheet1['D10'] = self.nationality
        sheet1['C12'] = self.entry
        sheet1['L12'] = self.entry
        sheet1['F12'] = self.departure
        sheet1['O12'] = self.departure
        sheet1['B16'] = str(self.familyname).upper() + '/'
        sheet1['B19'] = str(self.firstname).upper()
        sheet1['D16'] = str(self.name).upper() + '/'
        sheet1['D19'] = str(self.lastname).upper()
        sheet1['F16'] = date_format(self.birthday)
        sheet1['G17'] = str(self.sex).upper()
        sheet1['G16'] = self.passport
        sheet1['D21'] = str(self.goal).upper()
        #sheet1['D40'] = self.date
        #sheet1['M40'] = self.date
        sheet1['D25'] = self.placement
        sheet1['B27'],sheet1['B28'] = SplitOrganization(self.hostorganization)
        sheet1['F23'],sheet1['B24'] = SplitRout(self.rout)
        sheet1['E31'],sheet1['B32'],sheet1['B33'],sheet1['B34'] = SplitInfo(self.additionalinfo)

        # Внесение членов группы
        for i,g in enumerate(GroupMembers.objects.filter(form2=self)):
            for col in [0,9]:
                sheet1.cell(column=2+col,row=50+i*2).value = str(g.familyname).upper() + '/'
                sheet1.cell(column=2+col,row=51+i*2).value = str(g.name).upper()
                sheet1.cell(column=4+col,row=50+i*2).value = str(g.firstname).upper() + '/'
                sheet1.cell(column=4+col,row=51+i*2).value = str(g.lastname).upper()
                sheet1.cell(column=6+col,row=50+i*2).value = date_format(g.birthday)
                sheet1.cell(column=7+col,row=50+i*2).value = g.passport
                sheet1.cell(column=8+col,row=50+i*2).value = g.nationality


        ulr = openpyxl.styles.Border(
            top=openpyxl.styles.Side(style='thin'),
            left=openpyxl.styles.Side(style='thin'),
            right=openpyxl.styles.Side(style='thin'),
        )

        blr = openpyxl.styles.Border(
            bottom=openpyxl.styles.Side(style='thin'),
            left=openpyxl.styles.Side(style='thin'),
            right=openpyxl.styles.Side(style='thin'),
        )

        b = openpyxl.styles.Border(
            bottom=openpyxl.styles.Side(style='thin'),
        )

        t = openpyxl.styles.Border(
            top=openpyxl.styles.Side(style='thin'),
        )

        tlrb = openpyxl.styles.Border(
            top=openpyxl.styles.Side(style='thin'),
            left=openpyxl.styles.Side(style='thin'),
            right=openpyxl.styles.Side(style='thin'),
            bottom = openpyxl.styles.Side(style='thin')
        )

        for r in [14]+list(range(48, 70, 2)):
            for c in range(2,9):
                sheet1.cell(column=c,row = r).border = ulr
            for c in range(11, 18):
                sheet1.cell(column=c, row=r).border = ulr

        for r in [15] + list(range(49, 71, 2)):
            for c in range(2, 9):
                sheet1.cell(column=c, row=r).border = blr
            for c in range(11, 18):
                sheet1.cell(column=c, row=r).border = blr

        for r in [16,19,17,18]:
            for c in range(2,9):
                sheet1.cell(column=c, row=r).border = tlrb
            for c in range(11, 18):
                sheet1.cell(column=c, row=r).border = tlrb

        for r in [25]:
            for c in range(2,9):
                sheet1.cell(column=c, row=r).border = b
            for c in range(11, 18):
                sheet1.cell(column=c, row=r).border = b

        for r in [4,5]:
            for c in [72,74,39,41]:
                sheet1.cell(column=r, row=c).border = b

        for r in [13,14]:
            for c in [72,74,39,41]:
                sheet1.cell(column=r, row=c).border = b

        for c in range(2,18):
            sheet1.cell(column=45,row=c).border = t

        pech = openpyxl.drawing.image.Image('static/xlsx/image823.png')
        sheet1.add_image(pech, 'B35')
        pech2 = openpyxl.drawing.image.Image('static/xlsx/image823.png')
        sheet1.add_image(pech2, 'K35')
        pod = openpyxl.drawing.image.Image('static/xlsx/image853.png')
        sheet1.add_image(pod, 'D35')
        pod2 = openpyxl.drawing.image.Image('static/xlsx/image853.png')
        sheet1.add_image(pod2,'M35')

        pech = openpyxl.drawing.image.Image('static/xlsx/image823.png')
        sheet1.add_image(pech, 'B67')
        pech2 = openpyxl.drawing.image.Image('static/xlsx/image823.png')
        sheet1.add_image(pech2, 'K67')
        pod = openpyxl.drawing.image.Image('static/xlsx/image853.png')
        sheet1.add_image(pod, 'D67')
        pod2 = openpyxl.drawing.image.Image('static/xlsx/image853.png')
        sheet1.add_image(pod2,'M67')

    def GenerateXlsx(self,fout):
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename='+fout
        self.wb.save(response)
        #self.wb.save(filename='test.xlsx')
        return response

    def GeneratePdf(self,fout):
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename='+fout
        self.wb.save(response)
        return response



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

