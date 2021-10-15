from django import forms
from django.core.exceptions import ValidationError

from patientdiary.models import *


class PatientModelForm(forms.ModelForm):
    class Meta:
        fields = ['first_name', 'last_name', 'phone', 'clinic', 'my_history']
        model = Patient
        labels = {
            'first_name': 'imie',
            'last_name': 'nazwisko',
            'phone': 'telefon',
            'my_history': 'moja historia',
            'clinic': 'przychodnia'
        }


class DiseaseModelForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = '__all__'
        labels = {
            'name': 'nazwa',
            'description': 'opis'
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
            'name': 'nazwa',
            'leaflet': 'ulotka',
            'dosage': 'dawka',
            'action': 'działanie',
            'substances': 'substancja'
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
            'name': 'nazwa',
            'city': 'miasto',
            'street': 'ulica',
            'phone': 'numer telefonu'
        }


class PharmacyModelForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        fields = '__all__'
        labels = {
            'name': 'nazwa',
            'city': 'miasto',
            'street': 'ulica',
            'phone': 'numer telefonu',
            'opening_hours': 'godziny otwarcia'
        }


class DoctorModelForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        labels = {
            'first_name': 'imie',
            'last_name': 'imie',
            'medical_specialization': 'specjalizacja'
        }


