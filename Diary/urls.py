"""Diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from patientdiary import views

urlpatterns = [
    path('login/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', views.IndexView.as_view(), name='index_view'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('patient/', views.PatientListView.as_view(), name='patient_view'),
    path('patient/<int:pk>/', views.UpdatePatientView.as_view(), name='patient_update_view'),
    path('drugs/', views.DrugsListView.as_view(), name='drugs_view'),
    path('drugs/<int:pk>/', views.DrugDetailView.as_view(), name='drug_detail_view'),
    path('diseases/', views.DiseasesListView.as_view(), name='diseases_view'),
    path('diseases/<int:pk>/', views.DiseaseDetailView.as_view(), name='disease_detail_view'),
    path('contacts/', views.ContactsListView.as_view(), name='contacts'),
    path('add_drug/', views.AddDrugView.as_view(), name='drug_add_view'),
    path('add_disease/', views.AddDiseaseView.as_view(), name='disease_add_view'),
    path('delete_drug/<int:pk>/', views.DeleteDrugView.as_view(), name='drug_delete_view'),
    path('delete_disease/<int:pk>/', views.DeleteDiseaseView.as_view(), name='disease_delete_view'),
    path('update_drug/<int:pk>/', views.UpdateDrugView.as_view(), name='drug_update_view'),
    path('update_disease/<int:pk>/', views.UpdateDiseaseView.as_view(), name='disease_update_view'),

]
