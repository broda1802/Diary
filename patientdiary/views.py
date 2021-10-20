from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView

from accounts.models import CustomUser
from patientdiary.forms import DiseaseModelForm, DrugsModelForm, PatientModelForm, ClinicModelForm, PharmacyModelForm, \
    DoctorModelForm
from patientdiary.models import Drugs, Doctor, Disease, Clinic, Pharmacy, Group, Substance, Patient, PatientDisease


# Create your views here.


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        response = render(request, 'base.html', context={'patient': Patient.objects.get(user=self.request.user)})
        return response


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'patient_view.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class UpdatePatientView(LoginRequiredMixin, UpdateView):
    form_class = PatientModelForm
    model = Patient
    template_name = 'form.html'

    def get_success_url(self):
        return reverse_lazy('patient_view', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class ContactsListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        context['pharmacies'] = Pharmacy.objects.all()
        context['clinics'] = Clinic.objects.all()
        context['doctors'] = Doctor.objects.all()
        return context


class DiseasesListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Disease.objects.filter(patient=Patient.objects.get(user=self.request.user))
    model = Disease
    template_name = 'diseases_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class AddDiseaseView(LoginRequiredMixin, CreateView):
    model = Disease
    template_name = 'form.html'
    form_class = DiseaseModelForm
    success_url = "/diseases/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class AddPatientDiseaseView(LoginRequiredMixin, CreateView):
    model = PatientDisease
    template_name = 'form.html'
    # form_class = DiseaseModelForm
    success_url = "/diseases/"
    fields = ['disease']

    def form_valid(self, form):
        patient = Patient.objects.get(user=self.request.user)
        f = form.save(commit=False)
        f.patient = patient
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class DiseaseDetailView(LoginRequiredMixin, DetailView):
    model = Disease
    template_name = 'disease_detail_view.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class UpdateDiseaseView(LoginRequiredMixin, UpdateView):
    model = Disease
    template_name = 'form.html'
    form_class = DiseaseModelForm
    success_url = "/diseases/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class DeletePatientDiseaseView(LoginRequiredMixin, DeleteView):
    model = PatientDisease
    template_name = 'form.html'
    success_url = "/diseases/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        # context['disease'] = PatientDisease.objects.get(disease=self.kwargs['pk':])
        return context


class UpdatePatientDiseaseView(LoginRequiredMixin, UpdateView):
    model = PatientDisease
    template_name = 'form.html'
    fields = '__all__'
    success_url = "/diseases/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        # context['disease'] = PatientDisease.objects.get(disease=self.kwargs['pk':])
        return context


class DeleteDiseaseView(LoginRequiredMixin, DeleteView):
    model = Disease
    template_name = 'form.html'
    success_url = "/diseases/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class PatientDiseaseDetailView(LoginRequiredMixin, DetailView):
    model = PatientDisease
    template_name = 'patient_disease_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class DrugsListView(LoginRequiredMixin, ListView):
    model = Drugs
    template_name = 'drugs_view.html'

    def get_queryset(self):
        return Drugs.objects.filter(patient=Patient.objects.get(user=self.request.user))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class AddDrugView(LoginRequiredMixin, CreateView):
    model = Drugs
    template_name = 'form.html'
    form_class = DrugsModelForm
    success_url = "/drugs/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class DrugDetailView(LoginRequiredMixin, DetailView):
    model = Drugs
    template_name = 'drug_detail_view.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class UpdateDrugView(LoginRequiredMixin, UpdateView):
    model = Drugs
    template_name = 'form.html'
    form_class = DrugsModelForm
    success_url = "/drugs/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class DeleteDrugView(LoginRequiredMixin, DeleteView):
    model = Drugs
    template_name = 'form.html'
    success_url = "/drugs/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class AddClinicView(LoginRequiredMixin, CreateView):
    model = Clinic
    template_name = 'form.html'
    form_class = ClinicModelForm
    success_url = "/contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class UpdateClinicView(LoginRequiredMixin, UpdateView):
    model = Clinic
    template_name = 'form.html'
    form_class = ClinicModelForm
    success_url = "/contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class DeleteClinicView(LoginRequiredMixin, DeleteView):
    model = Clinic
    template_name = 'form.html'
    success_url = "/contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class AddPharmacyView(LoginRequiredMixin, CreateView):
    model = Pharmacy
    template_name = 'form.html'
    form_class = PharmacyModelForm
    success_url = "/contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class UpdatePharmacyView(LoginRequiredMixin, UpdateView):
    model = Pharmacy
    template_name = 'form.html'
    form_class = PharmacyModelForm
    success_url = "/contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class DeletePharmacyView(LoginRequiredMixin, DeleteView):
    model = Pharmacy
    template_name = 'form.html'
    success_url = "/contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class AddDoctorView(LoginRequiredMixin, CreateView):
    model = Doctor
    template_name = 'form.html'
    form_class = DoctorModelForm
    success_url = "/contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class UpdateDoctorView(LoginRequiredMixin, UpdateView):
    model = Doctor
    template_name = 'form.html'
    form_class = DoctorModelForm
    success_url = "/contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context


class DeleteDoctorView(LoginRequiredMixin, DeleteView):
    model = Doctor
    template_name = 'form.html'
    success_url = "/contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(user=self.request.user)
        return context

