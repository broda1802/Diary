import pytest
from django.contrib.auth.models import User

from patientdiary.models import Patient, Drugs, Disease


@pytest.fixture
def patients():
    lst = []
    for x in range(10):
        lst.append(Patient.objects.create(first_name=x, last_name=x))
    return lst

