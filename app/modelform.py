

from django.forms import *
from .models import *

bootstrap_class = 'form-control form-control-sm'
bootstrap_class_input_xs = 'form-control form-control-sm input-xs'

p = ['Фамилия (ru)', 'Фамилия (eng)', 'Имя, Отчество(ru)', 'Имя (eng)', 'Пол', 'Цель поездки',
     'Дата рождения', 'Номер паспорта', 'Въезд с', 'Выезд до', 'Гражданство', 'Кратность визы',
     'Подтверждение', 'Дата документа', 'Размещение', 'Маршрушт', 'Организация',
     'Дополнительная информация']

sex_choices = (
    ('мужской', 'мужской'),
    ('женский', 'женский'),
)
goal_choices = (
    ('туризм', 'туризм'),
)
multiplicity_choices = (
    ('однократная','однократная'),
    ('многократная','многократная')
)

class PartnerChoiceForm(ModelForm):
    partner_choice = ModelChoiceField(queryset=Partners.objects.all(),
                                    empty_label="Выбрать партнера",
                                    label="Партнер",
                                    widget=Select(attrs={'class': 'dropdown form-control form-control-sm'}),
                                    required=False,
                                    disabled=False)
    class Meta:
        model = Partners
        fields = ()

class InfoChoiceForm(ModelForm):
    info_choice = ModelChoiceField(queryset=AdditionalInfo.objects.all(),
                                   empty_label="Выбрать из списка",
                                   label='Выбрать из списка',
                                   widget=Select(attrs={'class': 'dropdown form-control form-control-sm'}),
                                   required=False,
                                   disabled=False)
    class Meta:
        model = AdditionalInfo
        fields = ()


class PlacementChoiceForm(ModelForm):
    placement_choice = ModelChoiceField(queryset=Placements.objects.all(),
                                   empty_label="Выбрать из списка",
                                   label='Выбрать из списка',
                                   widget=Select(attrs={'class': 'dropdown form-control form-control-sm'}),
                                   required=False,
                                   disabled=False)
    class Meta:
        model = Placements
        fields = ()
class NationalityChoiceForm(ModelForm):
    nationality_choice = ModelChoiceField(queryset=Nationality.objects.all(),
                                   empty_label="Выбрать из списка",
                                   label='Гражданство',
                                   widget=Select(attrs={'class': 'dropdown form-control form-control-sm'}),
                                   required=False,
                                   disabled=False)
    class Meta:
        model = Nationality
        fields = ()
class OrganizationChoiceForm(ModelForm):
    organization_choice = ModelChoiceField(queryset=Organizations.objects.all(),
                empty_label="Выбрать из списка",
                                           label='Выбрать из списка',
                widget=Select(attrs={'class': 'dropdown form-control form-control-sm'}),
                required=False,
                disabled=False,
                                           )
    class Meta:
        model = Organizations
        fields = ()
class RoutChoiceForm(ModelForm):
    rout_choice = ModelChoiceField(queryset=Routs.objects.all(),
                                   empty_label="Выбрать из списка",
                                   label='Выбрать из списка',
                                   widget=Select(attrs={'class': 'dropdown form-control form-control-sm'}),
                                   required=False,
                                   disabled=False)
    class Meta:
        model = Routs
        fields = ()
class ShipsChoiceForm(ModelForm):
    ship_choice = ModelChoiceField(queryset=Ships.objects.all(),
                                   empty_label="Выбрать из списка",
                                   label='Корабли из списка',
                                   widget=Select(attrs={'class': 'dropdown form-control form-control-sm'}),
                                   required=False,
                                   disabled=False)
    class Meta:
        model = Ships
        fields = ()
class DatesChoiceForm(ModelForm):
    date_choice = ModelChoiceField(queryset=Dates.objects.all(),
                                   empty_label="Выбрать из списка",
                                   label='Даты из списка',
                                   widget=Select(attrs={'class': 'dropdown form-control form-control-sm choice_action'}),
                                   required=False,
                                   disabled=False)
    class Meta:
        model = Dates
        fields = ()


class PartnerForm(ModelForm):
    class Meta:
        model = Partners
        fields = ('partner',)
        widgets = {
            'partner': TextInput(attrs={"class": bootstrap_class_input_xs, "placeholder": "Добавить партнера"}),
        }


class VisaNumberForm(ModelForm):
    class Meta:
        model = VisaNumber
        fields = ('visanumber',)
        widgets = {
            'visanumber' :  NumberInput()
        }


class NationalityForm(ModelForm):
    class Meta:
        model = Nationality
        fields = ('nationality',)
        widgets = {
            'nationality': TextInput(attrs={"class": bootstrap_class_input_xs, "placeholder": "Добавить гражданство"}),
        }
class OrganizationForm(ModelForm):
    class Meta:
        model = Organizations
        fields = ('organization',)
        widgets = {
            'organization': TextInput(attrs={"class": bootstrap_class_input_xs, "placeholder": "Добавить организации"}),
        }
class PlacementForm(ModelForm):
    class Meta:
        model = Placements
        fields = ('placement',)
        widgets = {
            'placement': TextInput(attrs={"class": bootstrap_class_input_xs, "placeholder": "Добавить размещение"}),
        }
class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ('info',)
        widgets = {
            'info': TextInput(attrs={"class": bootstrap_class_input_xs, "placeholder": "Добавить доп. информацию"}),
        }
class RoutsForm(ModelForm):
    class Meta:
        model = Routs
        fields = ('rout',)
        widgets = {
            'rout': TextInput(attrs={"class": bootstrap_class_input_xs, "placeholder": "Добавить маршрут"}),
        }
class ShipsForm(ModelForm):
    class Meta:
        model = Ships
        fields = ('name',)
        widgets = {
            'name': TextInput(attrs={"class": bootstrap_class_input_xs, "placeholder": 'Добавить название корабля'}),
        }
class DatesForm(ModelForm):
    date_choice = ModelChoiceField(queryset=Dates.objects,
                                   empty_label="Выбрать из списка",
                                   label='Даты из списка',
                                   widget=Select(attrs={'class': 'dropdown form-control form-control-sm'}),
                                   required=False)
    class Meta:
        model = Dates
        fields = ('ship','entry','departure')
        widgets = {
            'entry': DateInput(attrs={'class': bootstrap_class_input_xs,'type':'date'}),
            'departure': DateInput(attrs={'class': bootstrap_class_input_xs,'type':'date'}),
        }


class ModelForm2(ModelForm):
    #def __init__(self,*args, **kwargs):
        #super(ModelForm2,self).__init__(*args,**kwargs)
        #self.fields['confirmation'].required = False

    sex = ChoiceField(label="Пол",choices=sex_choices, widget=Select(attrs={"class": bootstrap_class}))
    goal = ChoiceField(label="Цель поездки", choices=goal_choices, widget=Select(attrs={"class": bootstrap_class}))
    multiplicity = ChoiceField(label="Кратность визы",choices=multiplicity_choices,widget=Select(attrs={"class": bootstrap_class}))
    class Meta:
        model = Form2
        exclude = ('visa_type',)

        widgets = {
            'name': TextInput(attrs={"class": bootstrap_class, "placeholder": p[2]}),
            'familyname': TextInput(attrs={"class": bootstrap_class, "placeholder": p[0]}),
            'firstname': TextInput(attrs={"class": bootstrap_class, "placeholder": p[1]}),
            'lastname': TextInput(attrs={"class": bootstrap_class, "placeholder": p[3]}),
            #'goal' : TextInput(attrs={"class": bootstrap_class,"placeholder":p[5]}),
            'birthday': DateInput(attrs={'class': bootstrap_class,'type':'date','max':'9999-12-30'}),
            'passport': TextInput(attrs={"class": bootstrap_class, "placeholder": p[7]}),
            'entry': DateInput(attrs={'class': bootstrap_class,'type':'date','max':'9999-12-30'}),
            'departure': DateInput(attrs={'class': bootstrap_class,'type':'date','max':'9999-12-30'}),
            'nationality': TextInput(attrs={"type":"hidden","class": bootstrap_class, "placeholder": p[10]}),
            'invitation_number': TextInput(attrs={"class": bootstrap_class}),
            'date': DateInput(attrs={'type':'hidden'}),
            'placement' : TextInput(attrs={'rows':2,"class":"form-control form-control-sm","placeholder": p[14]}),
            'rout': TextInput(attrs={'rows': 2, "class": "form-control form-control-sm","placeholder": p[15]}),
            'hostorganization': TextInput(attrs={'rows': 2, "class": "form-control form-control-sm","placeholder": p[16]}),
            'additionalinfo': TextInput(attrs={'rows': 2, "class": "form-control form-control-sm", "placeholder": p[17]}),
            'partner': TextInput(attrs={'type':'hidden'}),
        }
        labels = {
            'familyname': p[0],
            'firstname': p[1],
            'name': p[2],
            'lastname': p[3],
            'sex' :p[4],
            'goal': p[5],
            'birthday' : p[6],
            'passport' : p[7],
            'entry' : p[8],
            'departure' : p[9],
            'nationality' : p[10],
            'multiplicity' : p[11],
            'confirmation' : p[12],
            'date' : p[13],
            'placement':p[14],
            'rout':p[15],
            'hostorganization':p[16],
            'additionalinfo':p[17],
            'invitation_number': 'Приглашение №'
        }
class MembersForm(ModelForm):
    class Meta:
        model = GroupMembers
        bootstrap_class = 'form-control form-control-sm input-xs'
        exclude = ('order',)
        p = ['Фамилия (ru)', 'Фамилия (eng)', 'Имя (ru)', 'Имя (eng)',
             'Дата р-я', '№ паспорта','Гражданство']
        widgets = {
            'familyname': TextInput(attrs={"class": bootstrap_class+' familyname_class', "placeholder": p[0]}),
            'firstname': TextInput(attrs={"class": bootstrap_class+' firstname_class', "placeholder": p[1]}),
            'name': TextInput(attrs={"class": bootstrap_class+' name_class', "placeholder": p[2]}),
            'lastname': TextInput(attrs={"class": bootstrap_class + ' lastname_class', "placeholder": p[3]}),
            'birthday': DateInput(attrs={'class': bootstrap_class, 'type':'date'}),
            'passport': TextInput(attrs={"class": bootstrap_class, "placeholder": p[5]}),
            'nationality': TextInput(attrs={"class": bootstrap_class, "placeholder": p[6]}),
            }
        fields = (
            'firstname',
            'familyname',
            'lastname',
            'name',
            'birthday',
            'passport',
            'nationality'
        )

    def __init__(self,*args, **kwargs):
        super(MembersForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].required = True
