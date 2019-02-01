
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
        rec = Data()
        rec.grazhdanstvo = request.POST.get("grazhdanstvo")
        rec.kratnost = request.POST.get("kratnost")
        rec.grazhdanstvo2 = request.POST.get("grazhdanstvo2")
        rec.data_rozh = request.POST.get("data_rozh")
        rec.familiya = request.POST.get("familiya")
        rec.imya = request.POST.get("imya")
        rec.nomer_pass = request.POST.get("nomer_pass")
        rec.prin_organiz = request.POST.get("prin_organiz")
        rec.dop_svedeniya = request.POST.get("dop_svedeniya")
        rec.save()
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

