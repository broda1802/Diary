from django import forms
from django.core.exceptions import ValidationError

from patientdiary.models import *

class PatientForm(forms.Form):
    first_name = forms.CharField(label="imie")
    last_name = forms.CharField(label='nazwisko')
    Pesel = forms.IntegerField(label="Pesel")
    phone = forms.IntegerField(label="telefon")
    my_history = forms.CharField(widget=forms.Textarea)
    disease = forms.ModelMultipleChoiceField('Disease')
    drug = forms.ModelMultipleChoiceField('Drugs')
    clinic = forms.ModelChoiceField('Clinic', on_delete=models.CASCADE)


class Disease(forms.Form):
    name = forms.CharField(max_length=128, label="Nazwa choroby")
    description = forms.CharField(widget=forms.Textarea, label="opis choroby")


class Substance(forms.Form):
    substance_name = models.CharField(max_length=128)


class Drugs(forms.Form):
    name = forms.CharField(max_length=30, label="nazwa")
    leaflet = forms.CharField(widget=forms.Textarea, label="ulotka")
    dosage = forms.IntegerField(label="dawka")
    action = forms.CharField(max_length=128, label="działanie")
    substances = forms.ModelMultipleChoiceField(Substance, label="substancja")


class Group(forms.Form):
    parent = forms.ModelChoiceField('Group', null=True, on_delete=models.CASCADE)
    NAME = (
        ("A", "Przewód pokarmowy i metabolizm"),
        ("B", "Krew i układ krwiotwórczy"),
        ("C", "Układ sercowo-naczyniowy"),
        ("D", "Dermatologia"),
        ("G", "Układ moczowo-płciowy i hormony płciowe"),
        ("H", "Leki hormonalne do stosowania wewnętrznego"),
        ("J", "Leki przeciwinfekcyjne"),
        ("L",  "Leki przeciwnowotworowe i immunomodulujące"),
        ("M",  "Układ mięśniowo-szkieletowy"),
        ("N",  "Ośrodkowy układ nerwowy"),
        ("P", "Leki przeciwpasożytnicze, owadobójcze i repelenty"),
        ("R",  "Układ oddechowy"),
        ("S",  "Narządy wzroku i słuchu"),
        ("V",  "Różne")
    )
    name = forms.CharField(choices=NAME, max_length=128, label="grupa substancji")


class Clinic(forms.Form):
    name = forms.CharField(max_length=128, label="nazwa")
    city = forms.CharField(max_length=128, label="miasto")
    street = forms.CharField(max_length=50, label="ulica")
    phone = forms.IntegerField(label="numer telefonu")


class Pharmacy(forms.Form):
    name = forms.CharField(max_length=128, label="nazwa")
    city = forms.CharField(max_length=128, label="miasto")
    street = forms.CharField(max_length=50, label="ulica")
    phone = forms.IntegerField(label="telefon")
    opening_hours = forms.CharField(max_length=30, label="godziny otwarcia")


class Doctor(forms.Form):
    first_name = forms.CharField(max_length=30, label="imie")
    last_name = forms.CharField(max_length=30, label="nazwisko")
    medical_specialization = forms.CharField(max_length=30, label="specjalizacja")

