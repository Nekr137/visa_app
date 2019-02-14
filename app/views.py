
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseNotFound
from .modelform import ModelForm1, ModelForm2, MembersForm, DatesForm, ShipsForm, AdditionalInfoForm, RoutsForm, NationalityForm, DatesChoisesForm, PlacementForm, OrganizationForm
from .models import Form1, Form2, GroupMembers, Ships, Dates, AdditionalInfo, Nationality, Routs, Placements, Organizations
from django.core.paginator import Paginator
from django import forms
from django.forms import modelformset_factory


def edit_form2(request,id):
    # model
    model = Form2.objects.get(id=id)
    form = ModelForm2(prefix='0', instance=model)

    # members
    instance = GroupMembers.objects.filter(form2=model.id)

    if request.method == "POST":
        NUM = int(request.POST.get('NUM'))
        form = ModelForm2(request.POST,prefix='0',instance=model)

        # Разбираемся со старыми записями
        for i,inst in enumerate(instance):
            fm = MembersForm(request.POST, instance=inst, prefix="MEMBERFORM"+str(i))
            if fm.is_valid():
                fm.save()           # Обновляем
            else:
                inst.delete()       # Если не прошла валидацию, значит была удалена, значит удаляем из базы

        # Разбираемся со вновь добавленными записями (через ajax)
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
        member_forms = [MembersForm(prefix='MEMBERFORM' + str(i), instance=m) for i, m in enumerate(instance)]
        return render(request, "app/form2.html", {
            "form": form,
            "member_forms": member_forms,
            'NUM':len(instance),
            "title":"Редактирование формы групповой визы",
        })

def edit_form1(request,id):
    print('EDIT 1')
    model = Form1.objects.get(id=id)
    if request.method == "POST":
        form = ModelForm1(request.POST, instance=model)
        form.save()
        return redirect('/')
    else:
        form = ModelForm1(instance=model)
        return render(request, "app/form1.html", {
            "form": form,
            "title":"Редактирование формы одиночной визы"
        })



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
        elif type == 'placement':
            item = Placements.objects.get(id=id)
        elif type == 'organization':
            item = Organizations.objects.get(id=id)
        elif type == 'form1':
            item = Form1.objects.get(id=id)
            item.delete()
            return HttpResponseRedirect('/form1_db')
        elif type == 'form2':
            item = Form2.objects.get(id=id)
            item.delete()
            return HttpResponseRedirect('/form2_db')
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
        elif type == 'placement':
            form = PlacementForm(request.GET or None)
        elif type == 'organization':
            form = OrganizationForm(request.GET or None)
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
    return render(request,"app/lists.html",{
        'ships':Ships.objects.all(),
        'ships_mf':ShipsForm(),
        'infos':AdditionalInfo.objects.all(),
        'infos_mf':AdditionalInfoForm(),
        'routs':Routs.objects.all(),
        'routs_mf':RoutsForm(),
        'nationality':Nationality.objects.all(),
        'nationality_mf':NationalityForm(),
        'dates':Dates.objects.all(),
        'dates_mf':DatesForm(),
        'placements':Placements.objects.all(),
        'placements_mf':PlacementForm(),
        'organizations':Organizations.objects.all(),
        'organizations_mf':OrganizationForm()
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
        return render(request, "app/form1.html", {
            "form": ModelForm1(),
            "title":"Форма для одиночной визы",
            'Ships':Ships.objects.all(),
            'Routs' : Routs.objects.all(),
            'Nationality' : Nationality.objects.all(),
        })

def rewrite_dates_in_form(request):
    if request.method == "POST" and request.is_ajax():
        ship_id = request.POST.get('ship_id')
        dates_choice = DatesChoisesForm()
        dates_choice.fields['date_choice'].queryset = Dates.objects.filter(ship_id=ship_id)
        #dates_choice.fields['date_choice'].disabled = True
        #return HttpResponse(dates_choice)
        return render(request,'app/date_choice.html',{
            'dates_choice':dates_choice,
        })


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
            return HttpResponse('DATA INVALID')
    else:
        form = ModelForm2(prefix='0')
        return render(request, "app/form2.html", {
            "form": form,
            "title":"Форма для групповой визы",
        })

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
    paginator = Paginator(list, 10)
    page = request.GET.get('page') if request.method == "GET" else 1
    notes = paginator.get_page(page)
    return render(request,"app/form1_db.html",{'notes': notes,'list':list})



def form2_db(request):
    list = Form2.objects.all()
    paginator = Paginator(list, 10)
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

