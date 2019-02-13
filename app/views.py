
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseNotFound
from .modelform import ModelForm1, ModelForm2, MembersForm, DatesForm, ShipsForm, AdditionalInfoForm, RoutsForm, NationalityForm
from .models import Form1, Form2, GroupMembers, Ships, Dates, AdditionalInfo, Nationality, Routs
from django.core.paginator import Paginator
from django.forms import modelformset_factory


def del_item(request,type,id):
    if request.method == "GET":
        if type == 'ship':
            item = Ships.objects.get(id=id)
        elif type == 'date':
            item = Dates.objects.get(id=id)
        elif type == 'rout':
            item = Routs.objects.get(id=id)
        elif type == 'nationality':
            item = Nationality.objects.get(id=id)
        elif type == 'info':
            item = AdditionalInfo.objects.get(id=id)
        else:
            return HttpResponse('error')
        item.delete()
    return HttpResponseRedirect('/lists')



def add_item(request,type):
    if request.method == "GET":
        if type == 'ship':
            form = ShipsForm(request.GET or None)
        elif type == 'rout':
            form = RoutsForm(request.GET or None)
        elif type == 'nationality':
            form = NationalityForm(request.GET or None)
        elif type == 'info':
            form = AdditionalInfoForm(request.GET or None)
        elif type == 'date':
            ship_id = request.GET.get('ship')
            ship = Ships.objects.get(id=ship_id)
            form = DatesForm(request.GET or None)
            if form.is_valid():
                f = form.save(commit=False)
                f.ship = ship
                f.save()
        else:
            return HttpResponse('error')
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/lists')


def lists(request):
    ships = Ships.objects.all()
    ships_mf = ShipsForm()
    infos = AdditionalInfo.objects.all()
    infos_mf= AdditionalInfoForm()
    routs = Routs.objects.all()
    routs_mf = RoutsForm()
    nationality = Nationality.objects.all()
    nationality_mf = NationalityForm()
    dates = Dates.objects.all()
    dates_mf = DatesForm()
    return render(request,"app/lists.html",{
        'ships':ships,
        'ships_mf':ships_mf,
        'infos':infos,
        'infos_mf':infos_mf,
        'routs':routs,
        'routs_mf':routs_mf,
        'nationality':nationality,
        'nationality_mf':nationality_mf,
        'dates':dates,
        'dates_mf':dates_mf,

    })



def form1_xlsx(request):
    if request.method == "GET":
        id = request.GET.get('id')
        note = Form1.objects.get(id=id)
        response = note.GenerateXlsx(fin='static/xlsx/1.xlsx',fout='DATA.xlsx')
        return response


def form2_xlsx(request):
    if request.method == "GET":
        id = request.GET.get('id')
        note = Form2.objects.get(id=id)
        note.GenerateXlsx()
        return redirect('/')


def form1(request):
    if request.method == "POST":
        form = ModelForm1(request.POST)
        form.save()
        return redirect('/')
    else:
        form = ModelForm1()
        return render(request, "app/form1.html", {"form": form,"title":"Форма для одиночной визы"})


def form2(request):
    if request.method == "POST":
        NUM = int(request.POST.get('NUM'))
        form = ModelForm2(request.POST,prefix='0')

        if form.is_valid():
            f = form.save()
            f.save()
            for k in range(1,NUM+1):
                member_form = MembersForm(request.POST,prefix=str(k))
                if member_form.is_valid():
                    m = member_form.save(commit=False)
                    m.form2_id = f.id
                    m.save()
            return redirect('/')
    else:
        form = ModelForm2(prefix='0')
        return render(request, "app/form2.html", {
            "form": form,
            "title":"Форма для групповой визы",
        })



def form1_delete(request):
    if request.method == "GET":
        id = request.GET.get('id')
        note = Form1.objects.get(id=id)
        note.delete()
        return HttpResponseRedirect("/")



def form2_delete(request):
    if request.method == "GET":
        id = request.GET.get('id')
        note = Form2.objects.get(id=id)
        print('note = ',note)
        note.delete()
        return HttpResponseRedirect("/")


def add_member(request):
    if request.method == "POST" and request.is_ajax():
        NUM = request.POST['NUM']
        member = MembersForm(prefix=NUM)
        return render(request, "app/members_form.html", {"member": member, 'NUM':NUM})

def all_forms(request):
    return render(request,"app/all_forms.html")
    #return HttpResponse('app/all_forms.html')

def form1_db(request):
    list = Form1.objects.all()
    paginator = Paginator(list, 2)
    page = request.GET.get('page') if request.method == "GET" else 1
    notes = paginator.get_page(page)
    return render(request,"app/form1_db.html",{'notes': notes,'list':list})



def form2_db(request):
    list = Form2.objects.all()
    paginator = Paginator(list, 2)
    page = request.GET.get('page') if request.method == "GET" else 1
    notes = paginator.get_page(page)
    return render(request,"app/form2_db.html",{'notes': notes,'list':list})


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

