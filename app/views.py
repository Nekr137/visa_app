
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Data


# получение данных из бд
def index(request):
    records = Data.objects.all()
    return render(request, "index.html", {"records": records})

# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Data()
        tom.grazhdanstvo = request.POST.get("grazhdanstvo")
        tom.kratnost = request.POST.get("kratnost")
        tom.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        record = Data.objects.get(id=id)

        if request.method == "POST":
            print("POST")
            record.name = request.POST.get("name")
            record.age = request.POST.get("age")
            record.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"record": record})
    except Data.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Data.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Data.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

