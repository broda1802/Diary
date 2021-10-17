from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView

from accounts.models import CustomUser
from patientdiary.forms import DiseaseModelForm, DrugsModelForm, PatientModelForm
from patientdiary.models import Patient, Drugs, Doctor, Disease, Clinic, Pharmacy
# Create your views here.


class IndexView(View):
    def get(self, request):
        response = render(request, 'base.html', )
        return response


class PatientListView(PermissionRequiredMixin, ListView):
    permission_required = 'patientdiary.view_patient'
    model = Patient
    template_name = 'patient_view.html'


class DrugsListView(PermissionRequiredMixin, ListView):
    permission_required = 'patientdiary.view_drugs'
    model = Drugs
    template_name = 'drugs_view.html'


class DiseasesListView(PermissionRequiredMixin, ListView):
    permission_required = 'patientdiary.view_disease'
    model = Disease
    template_name = 'diseases_view.html'


class AddDrugView(PermissionRequiredMixin, CreateView):
    permission_required = 'patientdiary.add_drugs'
    model = Drugs
    template_name = 'form.html'
    form_class = DrugsModelForm
    success_url = "/drugs/"


class AddDiseaseView(PermissionRequiredMixin, CreateView):
    permission_required = 'patientdiary.add_disease'
    model = Disease
    template_name = 'form.html'
    form_class = DiseaseModelForm
    success_url = "/diseases/"


class ContactsListView(PermissionRequiredMixin, ListView):
    permission_required = 'patientdiary.view_pharmacy'
    model = CustomUser
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pharmacies'] = Pharmacy.objects.all()
        context['clinics'] = Clinic.objects.all()
        context['doctors'] = Doctor.objects.all()
        return context


class UpdateDiseaseView(PermissionRequiredMixin, UpdateView):
    permission_required = 'patientdiary.change_disease'
    model = Disease
    template_name = 'form.html'
    form_class = DiseaseModelForm

    success_url = "/diseases/"


class UpdatePatientView(PermissionRequiredMixin, UpdateView):
    permission_required = 'patientdiary.change_patient'
    form_class = PatientModelForm
    model = Patient
    template_name = 'form.html'
    success_url = "/patient/"


class UpdateDrugView(PermissionRequiredMixin, UpdateView):
    permission_required = 'patientdiary.change_drugs'
    model = Drugs
    template_name = 'form.html'
    form_class = DrugsModelForm
    success_url = "/drugs/"


class DeleteDiseaseView(PermissionRequiredMixin, DeleteView):
    permission_required = 'patientdiary.change_drugs'
    model = Disease
    template_name = 'form.html'
    success_url = "/diseases/"


class DeleteDrugView(PermissionRequiredMixin, DeleteView):
    permission_required = 'patientdiary.delete_drugs'
    model = Drugs
    template_name = 'form.html'
    success_url = "/drugs/"


class DiseaseDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'patientdiary.delete_disease'
    model = Disease
    template_name = 'disease_detail_view.html'
    fields = '__all__'


class DrugDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'patientdiary.view_drugs'
    model = Drugs
    template_name = 'drug_detail_view.html'
    fields = '__all__'


