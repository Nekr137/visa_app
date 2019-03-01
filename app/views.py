
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseNotFound
from .modelform import *
from .models import *
from django.core.paginator import Paginator
from datetime import date,datetime
from django.template.loader import get_template, render_to_string
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import View
import weasyprint
from django.template.loader import render_to_string, get_template


AppModels = {
    'ship': Ships,
    'date': Dates,
    'rout': Routs,
    'nationality': Nationality,
    'info': AdditionalInfo,
    'placement': Placements,
    'organization': Organizations,
    'form2':Form2,
    'partner':Partners,
}

AppModelforms = {
    'ship': ShipsForm,
    'date': DatesForm,
    'rout': RoutsForm,
    'nationality': NationalityForm,
    'info': AdditionalInfoForm,
    'placement': PlacementForm,
    'organization': OrganizationForm,
    'form2':ModelForm2,
    'partner':PartnerForm,
}

def statistic(request):
    return HttpResponse('statistic')



def html2pdf(request, id):
    note = Form2.objects.get(id=id)
    members = GroupMembers.objects.filter(form2=note)

    fname = note.firstname + '_' + note.lastname + '.pdf'

    html_string = render_to_string('app/form2_html.html', {
        'obj':note,
        'members':members,
        'empty_strings_len': 12-len(members),
        'date_now':datetime.now()
    })

    html = weasyprint.HTML(string=html_string,base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/mypdf.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + fname + '"'
        return response



def default(request,type,id):
    """ метод для изменения атрибута default у списков """
    if request.method == "GET":
        Model = AppModels[type]
        for i in Model.objects.filter(default=True):
            i.default = False
            i.save()
        item = Model.objects.get(id=id)
        item.default = True
        item.save()
    return HttpResponseRedirect('/lists')


def del_item(request,type,id):
    """ Метод для удаления элементов (списков илии форм) """
    Model = AppModels.get(type)                 # define a model
    if request.method == "GET" and Model:
        item = Model.objects.get(id=id)
        item.delete()
        if type == 'form2':
            resp = HttpResponseRedirect('/form2_db/id/False')
        else:
            resp = HttpResponseRedirect('/lists')
    else:
        resp = HttpResponse('error')
    return resp


def add_item(request,type):
    """ Метод для добавления элементов (в списках) """
    MF = AppModelforms.get(type)            # define a modelform
    if request.method == "GET" and MF:
        form = MF(request.GET or None)      # get form
        if form.is_valid():                 # check form
            if type == 'date':              # если имеем дело с вложенным списком (датами)
                ship = Ships.objects.get(id=request.GET.get('ship'))
                f = form.save(commit=False)
                f.ship = ship
                f.save()
            else:                           # иначе просто сохраняем
                form.save()
            resp = HttpResponseRedirect('/lists')
        else:
            resp = HttpResponse('error')
    else:
        resp = HttpResponse('error')
    return resp


def lists(request):
    """ Вывод всех списков """
    try:
        visa_number_form = VisaNumberForm(instance=VisaNumber.objects.get(id=1))
    except:
        visa_number_form = VisaNumberForm()

    return render(request,"app/lists.html",{
        'ships':Ships.objects.order_by('id'),
        'ships_mf':ShipsForm(),
        'infos':AdditionalInfo.objects.order_by('id'),
        'infos_mf':AdditionalInfoForm(),
        'routs':Routs.objects.order_by('id'),
        'routs_mf':RoutsForm(),
        'nationality':Nationality.objects.order_by('id'),
        'nationality_mf':NationalityForm(),
        'dates':Dates.objects.order_by('id'),
        'dates_mf':DatesForm(),
        'placements':Placements.objects.order_by('id'),
        'placements_mf':PlacementForm(),
        'organizations':Organizations.objects.order_by('id'),
        'organizations_mf':OrganizationForm(),
        'visa_mf':visa_number_form,
        'partners':Partners.objects.order_by('id'),
        'partners_mf':PartnerForm(),
    })


def rewrite_visanumber(request):
    if request.method == "GET":
        try:
            v = VisaNumberForm(request.GET, instance=VisaNumber.objects.get(id=1))
        except:
            v = VisaNumberForm(request.GET)
        v.save()
        return HttpResponseRedirect("/lists")

def increment_visanumber():
    try:
        obj = VisaNumber.objects.get(id=1)
        obj.visanumber += 1
        obj.save()
    except:
        v = VisaNumber()
        v.visanumber = 1
        v.save()
    return 1


def form2_xlsx(request):
    if request.method == "GET":
        id = request.GET.get('id')
        note = Form2.objects.get(id=id)
        print('ID = ',id)
        fname = note.firstname + '_' + note.lastname + '.xlsx'
        if note.visa_type == 'групповая':
            note.FormXlsx_group(fin='static/xlsx/2.xlsx')
        elif note.visa_type == 'одиночная':
            note.FormXlsx_single(fin='static/xlsx/1.xlsx')

        response = note.GenerateXlsx(fout=fname)
        return response


def form2_pdf(request):
    if request.method == "GET":
        id = request.GET.get('id')
        note = Form2.objects.get(id=id)
        fname = note.firstname + '_' + note.lastname + '.pdf'
        if note.visa_type == 'групповая':
            note.FormXlsx_group(fin='static/xlsx/2.xlsx')
        elif note.visa_type == 'одиночная':
            note.FormXlsx_single(fin='static/xlsx/1.xlsx')
        response = note.GeneratePdf(fout=fname)
        return response


def form2_html(request):
    return render(request,'app/form2_html.html')


def render_pdf_view(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'# find the template and render it.
    template = get_template('app/form2_html.html')
    html = template.render({'a':'b'})
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
        'orientation' : 'Landscape',
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    return response



def form2(request,visa_type):
    if request.method == "POST":
        form = ModelForm2(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            if visa_type == 'group':
                f.visa_type = 'групповая'
                f.save()
                for k in range(1,int(request.POST.get('NUM'))+1):
                    print("POST",request.POST)
                    print('K = ',k)
                    member_form = MembersForm(request.POST,prefix=str(k))
                    if member_form.is_valid():
                        m = member_form.save(commit=False)
                        m.form2_id = f.id
                        m.save()
            else:
                f.visa_type = 'одиночная'
                f.save()

            increment_visanumber()
            return redirect('/form2_db/id/False')
        else:
            return HttpResponse('person data invalid')

    else:
        # get list of dates
        date_choice = DatesChoiceForm()
        date_choice.fields['date_choice'].queryset = Dates.objects.filter(ship_id=get_default_object(Ships))

        # set default values
        def_data = {'date': date.today().strftime("%Y-%m-%d")}
        try:
            def_data['invitation_number'] = VisaNumber.objects.get(id=1)
        except:
            pass

        # load modelform
        form = ModelForm2(def_data)

        return render(request, "app/form2.html", {
            "form": form,
            "view": "form2",
            "NUM" : 1,
            "title" : 'Редактирование формы групповой визы' if visa_type=='group' else 'Редактирование формы одиночной визы',
            "date_choice": date_choice,
            "ship_choice": ShipsChoiceForm(initial={'ship_choice': get_default_object(Ships)}),
            "info_choice": InfoChoiceForm(initial={'info_choice': get_default_object(AdditionalInfo)}),
            "rout_choice": RoutChoiceForm(initial={'rout_choice': get_default_object(Routs)}),
            "organization_choice": OrganizationChoiceForm(initial={'organization_choice': get_default_object(Organizations)}),
            "nationality_choice": NationalityChoiceForm(initial={'nationality_choice': get_default_object(Nationality)}),
            "placement_choice": PlacementChoiceForm(initial={'placement_choice': get_default_object(Placements)}),
            "partner_choice": PartnerChoiceForm(initial={'partner_choice': get_default_object(Partners)}),
            "visa_type":visa_type,
        })

def edit_form2(request,id):
    # person
    model = Form2.objects.get(id=id)
    form = ModelForm2(instance=model)

    # members
    instance = GroupMembers.objects.filter(form2=model.id)

    visa_type = 'group' if model.visa_type == 'групповая' else 'single'

    if request.method == "POST":
        form = ModelForm2(request.POST, instance=model)

        if form.is_valid():
            f = form.save()
            f.save()
            #increment_visanumber() ???

            if visa_type == 'group':
            # Dealing with old group_members
                for i, inst in enumerate(instance):
                    fm = MembersForm(request.POST, instance=inst, prefix="MEMBERFORM" + str(i))
                    if fm.is_valid():
                        fm.save()  # update
                    else:
                        inst.delete()  # if not validated = was deleted

            # Dealing with just added (via ajax) group members
                for k in range(1,int(request.POST.get('NUM'))+1):
                    member_form = MembersForm(request.POST,prefix=str(k))
                    if member_form.is_valid():
                        m = member_form.save(commit=False)
                        m.form2_id = f.id
                        m.save()
            return redirect('/form2_db/id/False')
    else:
        member_forms = [MembersForm(prefix='MEMBERFORM' + str(i), instance=m) for i, m in enumerate(instance)]
        date_choice = DatesChoiceForm()
        date_choice.fields['date_choice'].queryset = Dates.objects.filter(ship_id=get_default_object(Ships))

        return render(request, "app/form2.html", {
            "form": form,
            "member_forms": member_forms,
            'NUM':len(instance),
            'visa_type': visa_type,
            "title" : 'Редактирование формы групповой визы' if visa_type=='group' else 'Редактирование формы одиночной визы',
            "view": "edit",
            "date_choice": date_choice,
            "ship_choice": ShipsChoiceForm(initial={'ship_choice': get_default_object(Ships)}),
            "info_choice": InfoChoiceForm(initial={'info_choice': get_default_object(AdditionalInfo)}),
            "rout_choice": RoutChoiceForm(initial={'rout_choice': get_default_object(Routs)}),
            "organization_choice": OrganizationChoiceForm(initial={'organization_choice': get_default_object(Organizations)}),
            "nationality_choice": NationalityChoiceForm(initial={'nationality_choice': get_default_object(Nationality)}),
            "placement_choice": PlacementChoiceForm(initial={'placement_choice': get_default_object(Placements)}),
            "partner_choice": PartnerChoiceForm(initial={'partner_choice': get_default_object(Partners)}),
        })

def get_default_object(Model):
    """ Отдает id объекта "списков", значение default которого True. Если такого нет, отдает 0 """
    try:
        return str(Model.objects.get(default=1).id)
    except:
        return '0'

def rewrite_dates_in_form(request):
    """
    Даты в формах зависят от выбора корабля. Поэтому после выбора корабля подгружаем
    ему соответствующие даты
    """
    if request.method == "POST" and request.is_ajax():
        dates_choice = DatesChoiceForm()
        dates_choice.fields['date_choice'].queryset = Dates.objects.filter(ship_id=request.POST.get('ship_id'))
        return render(request,"app/date_choice.html",{
            "date_choice" : dates_choice
        })

def add_member(request):
    if request.method == "POST" and request.is_ajax():
        NUM = request.POST['NUM']
        member = MembersForm(prefix=NUM)
        return render(request, "app/members_form.html", {"member": member, 'NUM':NUM})


def form2_db(request, sort_item='id', reverse='True'):
    """
    Show single and group visa forms
    :param request:
    :param sort_item: the viriable by wich to sort
    :param reverse: flag, signifying the direction ('True' or 'False')
    :return:
    """
    print(reverse)
    list = Form2.objects.order_by(sort_item,'id')
    list = list.reverse() if reverse=='True' else list
    paginator = Paginator(list, 10)
    page = request.GET.get('page') if request.method == "GET" else 1
    notes = paginator.get_page(page)
    return render(request,"app/form2_db.html",{
        'notes': notes,
        'reverse': 'True' if reverse=='False' else 'False'
    })

def index(request):
    """ Site main page """
    return render(request,"app/index.html")



