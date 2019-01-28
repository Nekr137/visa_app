
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Data


# получение данных из бд
def index(request):
    people = Data.objects.all()
    return render(request, "index.html", {"people": people})

# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Data()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        person = Data.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Data.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

