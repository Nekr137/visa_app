
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
#from .Forms import Form1
from .Xlsx import Xlsx
from pprint import pprint
from django.db import models
from .modelform import ModelForm1
from .models import Form1
from django.forms.formsets import formset_factory

def form1(request):
    form = ModelForm1()
    if request.method == "POST":
        print('\n\nPost reqeust from form1')
        f = request.POST.dict()
        pprint(f)
        #X = Xlsx('static/xlsx/1.xlsx')
        #X.WriteForm1(f1)
        #X.Save()

    return render(request, "app/form1.html", {"form": form})


# получение данных из бд
def index(request):
    form = ModelForm1()
    #FS = formset_factory(ModelForm1)
    #article = Form1.objects.get(pk=1)
    #form = ModelForm1(instance=article)
    if request.method == "POST":
        print('\n\nPost reqeust from form1')
        f = request.POST.dict()
        pprint(f)
        #X = Xlsx('static/xlsx/1.xlsx')
        #X.WriteForm1(f1)
        #X.Save()
    return render(request, "app/index.html", {"form": form})




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

