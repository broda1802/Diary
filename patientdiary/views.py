from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView

from accounts.models import CustomUser
from patientdiary.forms import DiseaseModelForm, DrugsModelForm
from patientdiary.models import Patient, Drugs, Doctor, Disease, Substance, Group, Clinic, Pharmacy
# Create your views here.

class IndexView(View):

    def get(self, request):
        response = render(request, 'base.html', )
        return response


class PatientListView(ListView):
    model = Patient
    template_name = 'patient_view.html'


class DrugsListView(ListView):
    model = Drugs
    template_name = 'drugs_view.html'


class DiseasesListView(ListView):
    model = Disease
    template_name = 'diseases_view.html'


class AddDrugView(CreateView):
    model = Drugs
    template_name = 'add_drug_view.html'
    form_class = DrugsModelForm


class AddDiseaseView(CreateView):
    model = Disease
    template_name = 'add_disease_view.html'
    form_class = DiseaseModelForm


class ContactsListView(ListView):

    model = CustomUser
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pharmacies'] = Pharmacy.objects.all()
        context['clinics'] = Clinic.objects.all()
        context['doctors'] = Doctor.objects.all()
        return context


class UpdateDiseaseView(UpdateView):
    model = Disease
    template_name = 'form.html'
    fields = '__all__'
    success_url = "/"


class UpdateDrugView(UpdateView):
    model = Drugs
    template_name = 'form.html'
    fields = '__all__'
    success_url = "/"



class DeleteDiseaseView(DeleteView):
    model = Drugs
    template_name = 'form.html'
    fields = '__all__'
    success_url = "/"


class DeleteDrugView(DeleteView):
    model = Drugs
    template_name = 'form.html'
    fields = '__all__'
    success_url = "/"


class DiseaseDetailView(DetailView):
    model = Drugs
    template_name = 'disease_detail_view.html'
    fields = '__all__'
    success_url = "/"


class DrugDetailView(DetailView):
    model = Drugs
    template_name = 'drug_detail_view.html'
    fields = '__all__'
    success_url = "/"
