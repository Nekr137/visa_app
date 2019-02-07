
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .Forms import Form1
from .Xlsx import Xlsx
from pprint import pprint
from django.db import models


def form1(request):
    if request.method == "POST":
        print('\n\nPost reqeust from form1')
        f = request.POST.dict()
        pprint(f)
        #X = Xlsx('static/xlsx/1.xlsx')
        #X.WriteForm1(f1)
        #X.Save()
        F = Form1.objects.create(
            confirmation = f.get('confirmation'),
            multiplicity = f.get('multiplicity'),
            nationality = f.get('nationality'),
            entry = f.get('entry'),
            departure = f.get('departure'),
            lastname = f.get('lastname'),
            familyname = f.get('familyname'),
            firstname = f.get('firstname'),
            name = f.get('name'),
            birthday = f.get('birthday'),
            sex = f.get('sex'),
            passport = f.get('passport'),
            goal = f.get('goal'),
            date = f.get('date'),
            placement = f.get('placement'),
            rout = f.get('rout'),
            hostorganization = f.get('hostorganization')
        )
        return render(request, "app/index.html", {"type": 1})
    else:
        return render(request, "app/form1.html", {"type": 1})


# получение данных из бд
def index(request):
    F = Form1()
    return render(request, "app/index.html", {"form1": F})




# изменение данных в бд
def edit(request, id):
    try:
        record = Form1.objects.get(id=id)

        if request.method == "POST":
            print("POST")
            record.name = request.POST.get("name")
            record.age = request.POST.get("age")
            record.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"record": record})
    except Form.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Data.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Data.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

