

from django.forms import ModelForm, Textarea, TextInput, DateField, DateInput, RadioSelect
from .models import Form1

SHIP_CHOICES = [
    ('akun','Viking Akun - АКУН'),
    ('truvor','Viking Truvor - ТРУВОР'),
    ('rurik','Viking Rurik - РЮРИК'),
    ('helgi','Vikig Helgi - ХЕЛЬГИ'),
    ('ingvar','Viking Ingvar - ИНГВАР'),
    ]

# Create the form class.
class ModelForm1(ModelForm):
    class Meta:
        model = Form1
        #fields = ['placement','firstname','lastname','name']
        bootstrap_class = 'form-control form-control-sm'
        exclude = ('order',)
        p = ['Фамилия','First name','Имя, Отчество (имена)','Last name','Пол','Цель поездки',
                   'Дата рождения','Номер паспорта','Въезд с','Выезд до','Гражданство','Кратность визы',
                   'Подтверждение №','Дата документа',
                   'Тип']
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
            'date': DateInput(format=('%d-%m-%Y'),attrs={'class': bootstrap_class,'type':'date'}),
            'type': RadioSelect(choices=SHIP_CHOICES,attrs={})
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
            'type': p[14]
        }


# Creating a form to add an article.
# form = ArticleForm()
#
# # Creating a form to change an existing article.
# article = Article.objects.get(pk=1)
# form = ArticleForm(instance=article)
