import pytest
from django.contrib.auth.models import User

from accounts.models import CustomUser
from patientdiary.models import Patient, Drugs, Disease


@pytest.fixture
def user():
    return CustomUser.objects.create(username='abc', password='xyz')
