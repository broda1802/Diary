import pytest
from django.test import Client
from django.urls import reverse

from accounts.models import CustomUser
from patientdiary.models import Drugs, Disease, Clinic, Pharmacy, Doctor


def test_login():
    client = Client()
    response = client.get(reverse("login"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_with_login(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('login'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout():
    client = Client()
    response = client.get(reverse('logout'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_signup():
    client = Client()
    response = client.get(reverse("signup"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_signup_post():
    client = Client()
    a = {
        'username': 'abc',
        'email': 'xyz@xyz.pl',
        'password1': 'laseczek1',
        'password2': 'laseczek1',
    }
    response = client.post(reverse("signup"), data=a)
    assert response.status_code == 302
    del a['password1']
    del a['password2']
    CustomUser.objects.get(**a)


@pytest.mark.django_db
def test_login_post(user):
    client = Client()
    a = {
        'username': 'xyz',
        'email': 'xyz@xyz.pl',
        'password1': 'laseczek1',
        'password2': 'laseczek1',
    }
    response = client.post(reverse("signup"), data=a)
    assert response.status_code == 302
    b = {
        'username': 'xyz',
        'password': 'laseczek1',
    }
    response = client.post(reverse("login"), data=b)
    assert response.status_code == 302


@pytest.mark.django_db
def test_index_view():
    client = Client()
    response = client.get(reverse('index_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_home_view():
    client = Client()
    response = client.get(reverse('home'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_contacts_not_logged():
    client = Client()
    response = client.get(reverse('contacts'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_contacts_logged(patient):
    client = Client()
    client.force_login(patient.user)
    response = client.get(reverse('contacts'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_patient_update_logged_get(user, patient):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('patient_update_view', kwargs={'pk': patient.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_drug_list_view_no_login():
    client = Client()
    response = client.get(reverse('drugs_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_drug_list_view_logged(patient):
    client = Client()
    client.force_login(patient.user)
    response = client.get(reverse('drugs_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_drug_delete_not_logged_get(drug):
    client = Client()
    response = client.get(reverse('drug_delete_view', kwargs={'pk': drug[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_drug_delete_logged_get(patient, drug):
    client = Client()
    client.force_login(patient.user)
    response = client.get(reverse('drug_delete_view', kwargs={'pk': drug[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_drug_delete_logged_post(patient, drug):
    client = Client()
    client.force_login(patient.user)
    response = client.post(reverse('drug_delete_view', kwargs={'pk': drug[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_drug_create_not_logged_get():
    client = Client()
    response = client.get(reverse('drug_add_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_drug_create_logged_get(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('drug_add_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_drug_create_logged_post(user, substance):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'Nazwa',
        'leaflet': 'Ulotka',
        'dosage': '1',
        'action': 'Działanie',
        'substances': substance[0].pk
    }
    response = client.post(reverse('drug_add_view'), data=a)
    assert response.status_code == 302
    Drugs.objects.get(**a)


@pytest.mark.django_db
def test_drug_update_logged_get(drug):
    client = Client()
    response = client.get(reverse('drug_update_view', kwargs={'pk': drug[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_drug_update_logged_get(user, drug):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('drug_update_view', kwargs={'pk': drug[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_drug_update_logged_post(user, substance, drug):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'Nazwa',
        'leaflet': 'Ulotka',
        'dosage': '1',
        'action': 'Działanie',
        'substances': substance[0].pk
    }
    response = client.post(reverse('drug_update_view', kwargs={'pk': drug[0].pk}), data=a)
    assert response.status_code == 302
    Drugs.objects.get(**a)


@pytest.mark.django_db
def test_drug_detail_logged(patient, drug):
    client = Client()
    client.force_login(patient.user)
    response = client.get(reverse('drug_detail_view', kwargs={'pk': drug[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_drug_detail_no_login(drug):
    client = Client()
    response = client.get(reverse('drug_detail_view', kwargs={'pk': drug[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_disease_list_view_no_login():
    client = Client()
    response = client.get(reverse('diseases_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_disease_list_view_logged(patient):
    client = Client()
    client.force_login(patient.user)
    response = client.get(reverse('diseases_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_disease_list_view_not_logged():
    client = Client()
    response = client.get(reverse('diseases_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_disease_delete_logged_get(patient, disease):
    client = Client()
    client.force_login(patient.user)
    response = client.get(reverse('disease_delete_view', kwargs={'pk': disease[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_disease_delete_logged_post(user, disease):
    client = Client()
    client.force_login(user)
    response = client.post(reverse('disease_delete_view', kwargs={'pk': disease[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_disease_create_not_logged_get():
    client = Client()
    response = client.get(reverse('disease_add_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_disease_create_logged_get(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('disease_add_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_disease_create_logged_post(user):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'Nazwa',
        'description': 'Opis'
    }
    response = client.post(reverse('disease_add_view'), data=a)
    assert response.status_code == 302
    Disease.objects.get(**a)


@pytest.mark.django_db
def test_disease_update_logged_get(user, disease):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('disease_update_view', kwargs={'pk': disease[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_disease_update_not_logged_get(disease):
    client = Client()
    response = client.get(reverse('disease_update_view', kwargs={'pk': disease[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_disease_update_logged_post(user, disease):
    client = Client()
    client.force_login(user)
    a = {'name': 'Nazwa',
         'description': 'Opis'
         }
    response = client.post(reverse('disease_update_view', kwargs={'pk': disease[0].pk}), data=a)
    assert response.status_code == 302
    Disease.objects.get(**a)


@pytest.mark.django_db
def test_disease_detail_logged(user, disease):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('disease_detail_view', kwargs={'pk': disease[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_disease_detail_not_logged(disease):
    client = Client()
    response = client.get(reverse('disease_detail_view', kwargs={'pk': disease[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_disease_detail_no_login(disease):
    client = Client()
    response = client.get(reverse('disease_detail_view', kwargs={'pk': disease[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_clinic_delete_logged_get(user, clinic):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('clinic_delete_view', kwargs={'pk': clinic[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_clinic_delete_logged_post(user, clinic):
    client = Client()
    client.force_login(user)
    response = client.post(reverse('clinic_delete_view', kwargs={'pk': clinic[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_clinic_create_not_logged_get():
    client = Client()
    response = client.get(reverse('clinic_add_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_clinic_create_logged_get(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('clinic_add_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_clinic_create_logged_post(user):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'Nazwa',
        'city': 'Miasto',
        'street': 'Ulica',
        'phone': '1'
    }
    response = client.post(reverse('clinic_add_view'), data=a)
    assert response.status_code == 302
    Clinic.objects.get(**a)


@pytest.mark.django_db
def test_clinic_update_logged_get(clinic):
    client = Client()

    response = client.get(reverse('clinic_update_view', kwargs={'pk': clinic[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_clinic_update_logged_get(user, clinic):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('clinic_update_view', kwargs={'pk': clinic[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_clinic_update_logged_post(user, clinic):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'Nazwa',
        'city': 'Miasto',
        'street': 'Ulica',
        'phone': '1'
    }
    response = client.post(reverse('clinic_update_view', kwargs={'pk': clinic[0].pk}), data=a)
    assert response.status_code == 302
    Clinic.objects.get(**a)


@pytest.mark.django_db
def test_pharmacy_create_not_logged_get():
    client = Client()
    response = client.get(reverse('pharmacy_add_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_pharmacy_create_logged_get(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('pharmacy_add_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_pharmacy_create_logged_post(user):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'Nazwa',
        'city': 'Miasto',
        'street': 'Ulica',
        'phone': '1',
        'opening_hours': 'Godziny otwarcia'
    }
    response = client.post(reverse('pharmacy_add_view'), data=a)
    assert response.status_code == 302
    Pharmacy.objects.get(**a)


@pytest.mark.django_db
def test_pharmacy_update_logged_get(pharmacy):
    client = Client()
    response = client.get(reverse('pharmacy_update_view', kwargs={'pk': pharmacy[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_pharmacy_update_logged_get(user, pharmacy):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('pharmacy_update_view', kwargs={'pk': pharmacy[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_pharmacy_update_logged_post(user, pharmacy):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'Nazwa',
        'city': 'Miasto',
        'street': 'Ulica',
        'phone': '1',
        'opening_hours': 'Godziny otwarcia'
    }
    response = client.post(reverse('pharmacy_update_view', kwargs={'pk': pharmacy[0].pk}), data=a)
    assert response.status_code == 302
    Pharmacy.objects.get(**a)


@pytest.mark.django_db
def test_pharmacy_delete_not_logged_get(pharmacy):
    client = Client()
    response = client.get(reverse('pharmacy_delete_view', kwargs={'pk': pharmacy[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_pharmacy_delete_logged_get(user, pharmacy):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('pharmacy_delete_view', kwargs={'pk': pharmacy[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_pharmacy_delete_logged_post(user, pharmacy):
    client = Client()
    client.force_login(user)
    response = client.post(reverse('pharmacy_delete_view', kwargs={'pk': pharmacy[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_doctor_create_not_logged_get():
    client = Client()
    response = client.get(reverse('doctor_add_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_doctor_create_logged_get(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('doctor_add_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_doctor_create_logged_post(user):
    client = Client()
    client.force_login(user)
    a = {
        'first_name': 'Imię',
        'last_name': 'Nazwisko',
        'medical_specialization': 'Specjalizacja'
    }
    response = client.post(reverse('doctor_add_view'), data=a)
    assert response.status_code == 302
    Doctor.objects.get(**a)


@pytest.mark.django_db
def test_pharmacy_update_not_logged_get(doctor):
    client = Client()
    response = client.get(reverse('doctor_update_view', kwargs={'pk': doctor[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_pharmacy_update_logged_get(user, doctor):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('doctor_update_view', kwargs={'pk': doctor[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_doctor_update_logged_post(user, doctor):
    client = Client()
    client.force_login(user)
    a = {
        'first_name': 'Imię',
        'last_name': 'Nazwisko',
        'medical_specialization': 'Specjalizacja'
    }
    response = client.post(reverse('doctor_update_view', kwargs={'pk': doctor[0].pk}), data=a)
    assert response.status_code == 302
    Doctor.objects.get(**a)


@pytest.mark.django_db
def test_doctor_delete_not_logged_get(doctor):
    client = Client()
    response = client.get(reverse('doctor_delete_view', kwargs={'pk': doctor[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_doctor_delete_logged_get(user, doctor):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('doctor_delete_view', kwargs={'pk': doctor[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_doctor_delete_logged_post(user, doctor):
    client = Client()
    client.force_login(user)
    response = client.post(reverse('doctor_delete_view', kwargs={'pk': doctor[0].pk}))
    assert response.status_code == 302

