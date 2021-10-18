import pytest
from django.test import Client
from django.urls import reverse

from accounts.models import Patient


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
def test_signup(user):
    client = Client()
    client.force_login(user)
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
    Patient.objects.get(**a)


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
def test_drug_list_view_no_login():
    client = Client()
    response = client.get(reverse('drugs_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_drug_list_view_logged(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('drugs_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_drug_delete_logged(user, drug):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('drug_delete_view', kwargs={'pk': drug[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_drug_delete_logged(user, drug):
    client = Client()
    client.force_login(user)
    response = client.post(reverse('drug_delete_view', kwargs={'pk': drug[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_drug_create_logged(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('drug_add_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_drug_create_logged(user, substance):
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












@pytest.mark.django_db
def test_disease_list_view_no_login():
    client = Client()
    response = client.get(reverse('diseases_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_disease_list_view_logged(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('diseases_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_disease_delete_logged(user, disease):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('disease_delete_view', kwargs={'pk': disease[0].pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_disease_delete_logged(user, disease):
    client = Client()
    client.force_login(user)
    response = client.post(reverse('disease_delete_view', kwargs={'pk': disease[0].pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_disease_create_logged(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('disease_add_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_disease_create_logged(user):
    client = Client()
    client.force_login(user)
    a = {
        'name': 'Nazwa',
        'description': 'Opis'
    }
    response = client.post(reverse('disease_add_view'), data=a)
    assert response.status_code == 302

