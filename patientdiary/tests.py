import pytest
from django.test import Client
from django.urls import reverse

from accounts.models import CustomUser


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


