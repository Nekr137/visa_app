
from django import forms


class Form1(forms.Form):
    familyname = forms.CharField(max_length=30)
    firstname = forms.CharField(max_length=30)
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    sex = forms.CharField(max_length=10)
    goal = forms.CharField(max_length=30)
    birthday = forms.DateField()
    passport = forms.Textarea()
    entry = forms.DateField()
    departure = forms.DateField()
    nationality = forms.Textarea()
    multiplicity = forms.Textarea()
    confirmation = forms.Textarea()
    date = forms.DateField()
    placement = forms.Textarea()
    rout = forms.Textarea()
    hostorganization = forms.Textarea()