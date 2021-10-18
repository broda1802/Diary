from django.contrib.auth.models import AbstractUser
from django.db import models
from patientdiary.models import Drugs, Disease, Clinic


class Patient(AbstractUser):
    Pesel = models.IntegerField(unique=True, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    my_history = models.TextField(null=True, blank=True)
    disease = models.ManyToManyField(Disease)
    drug = models.ManyToManyField(Drugs)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
