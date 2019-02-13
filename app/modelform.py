

from django.forms import ModelForm, Textarea, TextInput, DateField, DateInput, RadioSelect,CheckboxSelectMultiple, Textarea
from .models import Form1,Form2,GroupMembers, Dates, Ships, Routs, Nationality, AdditionalInfo
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms.models import BaseInlineFormSet

bootstrap_class = 'form-control form-control-sm'
bootstrap_class_input_xs = 'form-control form-control-sm input-xs'


class NationalityForm(ModelForm):
    class Meta:
        model = Nationality
        fields = ('nationality',)
        widgets = {
            'nationality': TextInput(attrs={"class": bootstrap_class_input_xs, "placeholder": "Добавить гражданство"}),
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
    class Meta:
        model = Dates
        fields = ('ship','entry','departure')
        widgets = {
            'entry': DateInput(format=('%d-%m-%Y'),attrs={'class': bootstrap_class_input_xs,'type':'date'}),
            'departure': DateInput(format=('%d-%m-%Y'),attrs={'class': bootstrap_class_input_xs,'type':'date'}),
        }

class ModelForm1(ModelForm):
    class Meta:
        model = Form1
        exclude = ('order',)
        p = ['Фамилия','First name','Имя, Отчество (имена)','Last name','Пол','Цель поездки',
                   'Дата рождения','Номер паспорта','Въезд с','Выезд до','Гражданство','Кратность визы',
                   'Подтверждение №','Дата документа','Размещение','Маршрушт','Принимающая организация']
        widgets = {
            'familyname': TextInput(attrs={"class": bootstrap_class, "placeholder":p[0]}),
            'firstname': TextInput(attrs={"class": bootstrap_class,"placeholder":p[1]}),
            'name': TextInput(attrs={"class": bootstrap_class,"placeholder": p[2]}),
            'lastname': TextInput(attrs={"class": bootstrap_class,"placeholder":p[3]}),
            'sex' : TextInput(attrs={"class": bootstrap_class,"placeholder":p[4]}),
            'goal' : TextInput(attrs={"class": bootstrap_class,"placeholder":p[5]}),
            'birthday': DateInput(format=('%d-%m-%Y'),attrs={'class': bootstrap_class,'type':'date'}),
            'passport': TextInput(attrs={"class": bootstrap_class, "placeholder": p[7]}),
            'entry': DateInput(format=('%d-%m-%Y'),attrs={'class': bootstrap_class,'type':'date'}),
            'departure': DateInput(format=('%d-%m-%Y'),attrs={'class': bootstrap_class,'type':'date'}),
            'nationality': TextInput(attrs={"class": bootstrap_class, "placeholder": p[10]}),
            'multiplicity': TextInput(attrs={"class": bootstrap_class, "placeholder": p[11]}),
            'confirmation': TextInput(attrs={"class": bootstrap_class, "placeholder": p[12]}),
            'date': DateInput(format=('%d-%m-%Y'),attrs={'class': bootstrap_class,'type':'date','placeholder':p[13]}),
            'placement' : Textarea(attrs={'rows':2,"class":"form-control form-control-sm","placeholder": p[14]}),
            'rout': Textarea(attrs={'rows': 2, "class": "form-control form-control-sm","placeholder": p[15]}),
            'hostorganization': Textarea(attrs={'rows': 2, "class": "form-control form-control-sm","placeholder": p[16]})
            #'type': RadioSelect(choices=SHIP_CHOICES,attrs={}),
            #'type2': CheckboxSelectMultiple(choices = SHIP_CHOICES)
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
            'hostorganization':p[16]
        }

class ModelForm2(ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            },
        }
        model = Form2
        bootstrap_class = 'form-control form-control-sm'
        exclude = ('order',)
        p = ['Фамилия','First name','Имя, Отчество','Last name','Пол','Цель поездки',
                   'Дата рождения','№ паспорта','Въезд с','Выезд до','Гражданство','Кратность визы',
                   'Подтверждение №','Дата документа','Размещение','Маршрушт','Принимающая организация']
        widgets = {
            'familyname': TextInput(attrs={"class": bootstrap_class, "placeholder":p[0]}),
            'firstname': TextInput(attrs={"class": bootstrap_class,"placeholder":p[1]}),
            'name': TextInput(attrs={"class": bootstrap_class,"placeholder": p[2]}),
            'lastname': TextInput(attrs={"class": bootstrap_class,"placeholder":p[3]}),
            'sex' : TextInput(attrs={"class": bootstrap_class,"placeholder":p[4]}),
            'goal' : TextInput(attrs={"class": bootstrap_class,"placeholder":p[5]}),
            'birthday': DateInput(format=('%d-%m-%Y'),attrs={'class': bootstrap_class,'type':'date'}),
            'passport': TextInput(attrs={"class": bootstrap_class, "placeholder": p[7]}),
            'entry': DateInput(format=('%d-%m-%Y'),attrs={'class': bootstrap_class,'type':'date'}),
            'departure': DateInput(format=('%d-%m-%Y'),attrs={'class': bootstrap_class,'type':'date'}),
            'nationality': TextInput(attrs={"class": bootstrap_class, "placeholder": p[10]}),
            'multiplicity': TextInput(attrs={"class": bootstrap_class, "placeholder": p[11]}),
            'confirmation': TextInput(attrs={"class": bootstrap_class, "placeholder": p[12]}),
            'date': DateInput(format=('%d-%m-%Y'),attrs={'class': bootstrap_class,'type':'date','placeholder':p[13]}),
            'placement' : Textarea(attrs={'rows':2,"class":"form-control form-control-sm","placeholder": p[14]}),
            'rout': Textarea(attrs={'rows': 2, "class": "form-control form-control-sm","placeholder": p[15]}),
            'hostorganization': Textarea(attrs={'rows': 2, "class": "form-control form-control-sm","placeholder": p[16]})
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
            'hostorganization':p[16]
        }

class MembersForm(ModelForm):
    class Meta:
        model = GroupMembers
        bootstrap_class = 'form-control form-control-sm input-xs'
        exclude = ('order',)
        p = ['Фамилия', 'First name', 'Имя, отчество', 'Last name',
             'Дата р-я', '№ паспорта','Гражданство']
        widgets = {
            'familyname': TextInput(attrs={"class": bootstrap_class, "placeholder": p[0]}),
            'firstname': TextInput(attrs={"class": bootstrap_class, "placeholder": p[1]}),
            'name': TextInput(attrs={"class": bootstrap_class, "placeholder": p[2]}),
            'lastname': TextInput(attrs={"class": bootstrap_class, "placeholder": p[3]}),
            'birthday': DateInput(format=('%d-%m-%Y'), attrs={'class': bootstrap_class, 'type':'date'}),
            'passport': TextInput(attrs={"class": bootstrap_class, "placeholder": p[5]}),
            'nationality': TextInput(attrs={"class": bootstrap_class, "placeholder": p[6]}),
            }
        fields = (
            'familyname',
            'firstname',
            'name',
            'lastname',
            'birthday',
            'passport',
            'nationality'
        )
        # labels = {
        #     'familyname': p[0],
        #     'firstname': p[1],
        #     'name': p[2],
        #     'lastname': p[3],
        #     'birthday': p[4],
        #     'passport': p[5],
        #     'nationality': p[6],
        # }

    def __init__(self,*args, **kwargs):
        super(MembersForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].required = True
        #
        # self.fields['familyname'].required = True
        # self.fields['firstname'].required = True
        # self.fields['name'].required = True

