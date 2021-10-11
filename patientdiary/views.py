from django.shortcuts import render
from django.views import View

from patientdiary.models import Patient, Drugs, Doctor, Disease, Substance, Group, Clinic, Pharmacy
# Create your views here.

class IndexView(View):

    def get(self, request):
        response = render(request, 'base.html')
        return response


# class PatientView(View):

