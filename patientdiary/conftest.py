import pytest
from accounts.models import CustomUser
from patientdiary.models import Drugs, Disease, Substance, Group, Clinic, Pharmacy, Doctor, Patient
from faker import Faker

faker = Faker("pl_PL")


@pytest.fixture
def user():
    return CustomUser.objects.create(username='abc', password='laseczek1')


@pytest.fixture
def patient(disease, drug, clinic, user):
    lst = []
    for x in range(10):
        p = Patient.objects.create(user=user[0], first_name=faker.text(max_nb_chars=20),
                                   last_name=faker.text(max_nb_chars=20), Pesel=1234, phone=12345,
                                   my_history=faker.text(max_nb_chars=20), clinic=clinic[0])
        p.disease.set(disease)
        p.drug.set(drug)
        lst.append(p)

    return lst


@pytest.fixture
def disease():
    lst = []
    for p in range(10):
        lst.append(Disease.objects.create(name=faker.text(max_nb_chars=20), description=faker.text(max_nb_chars=20),
                                          ))
    return lst


@pytest.fixture
def drug(substance):
    lst = []
    for p in range(10):
        p = Drugs.objects.create(name=faker.text(max_nb_chars=20), leaflet=faker.text(max_nb_chars=20),
                                 dosage=1, action=faker.text(max_nb_chars=20),
                                 )
        p.substances.add(substance[0])
        lst.append(p)
    return lst


@pytest.fixture
def substance():
    lst = []
    for p in range(10):
        lst.append(Substance.objects.create(substance_name=faker.text(max_nb_chars=20)))
    return lst


@pytest.fixture
def group():
    lst = []
    for p in range(10):
        lst.append(Group.objects.create(symbol=faker.text(max_nb_chars=20),
                                        name=faker.text(max_nb_chars=20)))
    return lst


@pytest.fixture
def clinic():
    lst = []
    for p in range(10):
        lst.append(Clinic.objects.create(name=faker.text(max_nb_chars=20), city=faker.text(max_nb_chars=20),
                                         street=faker.text(max_nb_chars=20), phone=1))
    return lst


@pytest.fixture
def pharmacy():
    lst = []
    for p in range(10):
        lst.append(Pharmacy.objects.create(name=faker.text(max_nb_chars=20), city=faker.text(max_nb_chars=20),
                                           street=faker.text(max_nb_chars=20), phone=1, opening_hours=1))
    return lst


@pytest.fixture
def doctor():
    lst = []
    for p in range(10):
        lst.append(Doctor.objects.create(first_name=faker.text(max_nb_chars=20), last_name=faker.text(max_nb_chars=20),
                                         medical_specialization=faker.text(max_nb_chars=20)))
    return lst


