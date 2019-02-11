
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseNotFound
from .Xlsx import Xlsx
from pprint import pprint
from django.db import models
from .modelform import ModelForm1, ModelForm2, MembersForm
from .models import Form1, Form2, GroupMembers
from django.forms.formsets import formset_factory
from django.forms.models import model_to_dict, modelformset_factory, inlineformset_factory

def form1(request):
    if request.method == "POST":
        print("view/vorm1 post")
        #X = Xlsx('static/xlsx/1.xlsx')
        #X.WriteForm1(f1)
        #X.Save()
        form = ModelForm1(request.POST)
        form.save()
        return redirect('/')
    else:
        print('view/form1 request')
        form = ModelForm1()
        return render(request, "app/form1.html", {"form": form,"title":"Форма для одиночной визы"})


def form2(request):
    if request.method == "POST":
        extra = request.POST.get('groupmembers_set-TOTAL_FORMS')
        extra = 5
        MemberInlineFormset = inlineformset_factory(Form2, GroupMembers, MembersForm, extra=3, can_delete=False, )
        form = ModelForm2(request.POST)

        if form.is_valid():
            created_form = form.save(commit=False)
            formset = MemberInlineFormset(request.POST or None, instance=created_form)

            if formset.is_valid():
                created_form.save()
                formset.save()
            return redirect('/')
        else:
            return HttpResponse("Invalid data")


    else:
        form = ModelForm2()
        MemberInlineFormset = inlineformset_factory(Form2, GroupMembers, MembersForm, extra=1, can_delete=False)
        members_set = MemberInlineFormset()
        NUM = 1
        return render(request, "app/form2.html", {
            "form": form,
            "members_set": members_set,
            "title":"Форма для групповой визы",
            "NUM":NUM
        })


def add_member(request):
    if request.method == "POST" and request.is_ajax():
        NUM = request.POST['NUM']
        MemberInlineFormset = inlineformset_factory(Form2, GroupMembers, MembersForm, extra=1, can_delete=False)
        members_set = MemberInlineFormset()
        #return HttpResponse(members_set)
        return render(request, "app/members_form.html", {"members_set2": members_set, 'NUM':NUM})

def all_forms(request):
    data = Form1.objects.all()
    P = ['Фамилия', 'First name', 'Имя, Отчество', 'Last name', 'Пол', 'Цель поездки',
         'Дата рождения', 'Номер паспорта', 'Въезд с', 'Выезд до', 'Гражданство', 'Кратность визы',
         'Подтверждение №', 'Дата документа', 'Размещение', 'Маршрушт', 'Принимающая организация']
    return render(request,"app/all_forms.html", {"data":data,"P":P})

# получение данных из бд
def index(request):
    return render(request,"app/index.html")



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

