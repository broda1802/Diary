import pytest
from accounts.models import CustomUser
from patientdiary.models import Drugs, Disease, Substance, Group, Clinic, Pharmacy, Doctor, Patient, PatientDisease, \
    PatientDrug
from faker import Faker

faker = Faker("pl_PL")


@pytest.fixture
def user():
    user = CustomUser.objects.create_user(username="heniek", email="email", password="password1")
    return user


@pytest.fixture
def users():
    lst = []
    for x in range(10):
        lst.append(CustomUser.objects.create(username=x, password='laseczek1'))
    return lst


@pytest.fixture
def patient(disease, drug, clinic, user):
    p = Patient.objects.create(user=user, first_name=faker.text(max_nb_chars=20),
                               last_name=faker.text(max_nb_chars=20), Pesel=1234, phone=12345,
                               my_history=faker.text(max_nb_chars=20), clinic=clinic[0])

    return p


@pytest.fixture
def patients(disease, drug, clinic, users):
    lst = []
    for user in users:
        p = Patient.objects.create(user=user, first_name=faker.text(max_nb_chars=20),
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
def drug(substance, group):
    lst = []
    for p in range(10):
        p = Drugs.objects.create(name=faker.text(max_nb_chars=20), leaflet=faker.text(max_nb_chars=20),
                                 dosage=1, action=faker.text(max_nb_chars=20), groups=group[0]
                                 )
        p.substances.add(substance[0])
        lst.append(p)
    return lst


@pytest.fixture
def patient_disease(patient, disease):
    patient_disease = PatientDisease.objects.create(patient=patient, disease=disease[0])
    return patient_disease


@pytest.fixture
def patient_drug(patient, drug):
    patient_drug = PatientDrug.objects.create(patient=patient, drug=drug[0])
    return patient_drug


@pytest.fixture
def substance():
    lst = []
    for p in range(10):
        lst.append(Substance.objects.create(name=faker.text(max_nb_chars=20)))
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


