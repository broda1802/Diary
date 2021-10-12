from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from accounts.models import CustomUser
from patientdiary.models import Patient, Drugs, Doctor, Disease, Substance, Group, Clinic, Pharmacy
# Create your views here.

class IndexView(View):

    def get(self, request):
        response = render(request, 'base.html', )
        return response


class PatientView(View):
    pass


class DrugsView(View):
    pass


class DiseasesView(View):
    pass


class AddDrugView(View):
    pass


class AddDiseaseView(View):
    pass


# class ContactsView(DetailView):
#
#     def get(self, request):
#         pharmacies = Pharmacy.objects.all()
#         clinic = Clinic.objects.all()
#         doctor = Doctor.objects.all()
#         return render(request, 'contacts.html',{'pharmacies': pharmacies,
#                                                 'clinic': clinic,
#                                                 'doctor': doctor}
#                       )
#
# class ContactsView(ListView):
#
#     model = CustomUser
#     template_name = 'contacts.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['pharmacies'] = Pharmacy.objects.all()
#         context['clinic'] = Clinic.objects.all()
#         context['doctor'] = Doctor.objects.all()
#         return context


class DoctorView(View):
    pass


class PharmacyView(View):
    pass


class ClinicView(View):
    pass

