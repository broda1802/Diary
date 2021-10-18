from django import forms

from accounts.models import Patient
from patientdiary.models import *


class PatientModelForm(forms.ModelForm):
    class Meta:
        fields = ['first_name', 'last_name', 'phone', 'clinic', 'my_history']
        model = Patient
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'phone': 'Numer telefonu',
            'my_history': 'Moja historia chorób',
            'clinic': 'Moja przychodnia'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'my_history': forms.Textarea(attrs={'class': 'form-control'}),
            'clinic': forms.Select(attrs={'class': 'form-control'})
        }


class DiseaseModelForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = '__all__'
        labels = {
            'name': 'Nazwa',
            'description': 'Opis'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SubstanceModelForm(forms.ModelForm):
    class Meta:
        model = Substance
        fields = '__all__'
        labels = {
            'substance_name': 'nazwa substancji'
        }


class DrugsModelForm(forms.ModelForm):
    class Meta:
        model = Drugs
        fields = '__all__'
        labels = {
            'name': 'Nazwa',
            'leaflet': 'Ulotka',
            'dosage': 'Dawka',
            'action': 'Działanie',
            'substances': 'Substancja'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'leaflet': forms.Textarea(attrs={'class': 'form-control'}),
            'dosage': forms.NumberInput(attrs={'class': 'form-control'}),
            'action': forms.TextInput(attrs={'class': 'form-control'}),
            'substances': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class GroupModelForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        labels = {
            'parent': 'grupa',
            'name': 'nazwa grupy',
            'symbol': 'symbol'
        }


class ClinicModelForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = '__all__'
        labels = {
            'name': 'Nazwa',
            'city': 'Miasto',
            'street': 'Ulica',
            'phone': 'Numer telefonu'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'})

        }


class PharmacyModelForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        fields = '__all__'
        labels = {
            'name': 'Nazwa',
            'city': 'Miasto',
            'street': 'Ulica',
            'phone': 'Numer telefonu',
            'opening_hours': 'Godziny otwarcia'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'opening_hours': forms.TextInput(attrs={'class': 'form-control'})
        }


class DoctorModelForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'medical_specialization': 'Specjalizacja'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'medical_specialization': forms.TextInput(attrs={'class': 'form-control'})
        }


