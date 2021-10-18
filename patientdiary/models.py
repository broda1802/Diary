from django.db import models

# Create your models here.
from django.urls import reverse


class Disease(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('disease_detail_view', args=(self.pk,))

    def get_delete_url(self):
        return reverse('disease_delete_view', args=(self.pk,))

    def __str__(self):
        return self.name


class Substance(models.Model):
    substance_name = models.CharField(max_length=128)

    def __str__(self):
        return self.substance_name


class Drugs(models.Model):
    name = models.CharField(max_length=30)
    leaflet = models.TextField()
    dosage = models.IntegerField()
    action = models.CharField(max_length=128)
    substances = models.ManyToManyField(Substance)

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

