
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Form1
from .Xlsx import Xlsx
from pprint import pprint


def form1(request):
    if request.method == "POST":
        print('Post reqeust from form1')
        f1 = request.POST.dict()
        pprint(f1)

        return render(request, "app/form1.html", {"type": 1})
    else:
        return render(request, "app/form1.html", {"type": 1})


# получение данных из бд
def index(request):
    records = Form1.objects.all()
    return render(request, "app/index.html", {"records": records})




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

