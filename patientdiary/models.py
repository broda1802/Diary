from django.db import models

# Create your models here.
from django.urls import reverse
from accounts.models import CustomUser


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True, blank=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    Pesel = models.IntegerField(unique=True, null=True)
    phone = models.IntegerField(null=True)
    my_history = models.TextField(null=True)
    disease = models.ManyToManyField('Disease', blank=True, through='PatientDisease')
    drug = models.ManyToManyField('Drugs', blank=True, through='PatientDrug')
    clinic = models.ForeignKey('Clinic', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_substance_alert(self):
        alerts = {}
        for drug in self.drug.all():
            for substance in drug.substances.all():
                if substance.name in alerts:
                    alerts[substance.name].append(drug.name)
                else:
                    alerts[substance.name] = [drug.name]
        return alerts


class PatientDisease(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey('Disease', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.disease.name


class PatientDrug(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    drug = models.ForeignKey('Drugs', on_delete=models.CASCADE)

    def __str__(self):
        return self.drug.name


class Disease(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('disease_detail_view', args=(self.pk,))

    def get_delete_url(self):
        return reverse('disease_delete_view', args=(self.pk,))

    def get_update_url(self):
        return reverse('disease_update_view', args=(self.pk,))

    def __str__(self):
        return self.name


class Substance(models.Model):
    name = models.CharField(unique=True, max_length=128)

    def __str__(self):
        return self.name


class Drugs(models.Model):
    name = models.CharField(max_length=30)
    leaflet = models.TextField()
    dosage = models.DecimalField(max_digits=10, decimal_places=2)
    action = models.CharField(max_length=128)
    substances = models.ManyToManyField(Substance)
    groups = models.ForeignKey('Group', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('drug_detail_view', args=(self.pk,))

    def get_delete_url(self):
        return reverse('drug_delete_view', args=(self.pk,))

    def __str__(self):
        return self.name


class Group(models.Model):
    parent = models.ForeignKey('Group', null=True, blank=True, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Clinic(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Pharmacy(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=50)
    phone = models.IntegerField()
    opening_hours = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    medical_specialization = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name
