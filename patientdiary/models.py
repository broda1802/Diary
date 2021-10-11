from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Pesel = models.IntegerField(unique=True)
    phone = models.IntegerField()
    my_history = models.TextField()
    disease = models.ManyToManyField('Disease')
    drug = models.ManyToManyField('Drugs')
    clinic = models.ForeignKey('Clinic', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Disease(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

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

    def __str__(self):
        return self.name


class Group(models.Model):
    parent = models.ForeignKey('Group', null=True, on_delete=models.CASCADE)
    NAME = (
        ("A", "Przewód pokarmowy i metabolizm"),
        ("B", "Krew i układ krwiotwórczy"),
        ("C", "Układ sercowo-naczyniowy"),
        ("D", "Dermatologia"),
        ("G", "Układ moczowo-płciowy i hormony płciowe"),
        ("H", "Leki hormonalne do stosowania wewnętrznego"),
        ("J", "Leki przeciwinfekcyjne"),
        ("L",  "Leki przeciwnowotworowe i immunomodulujące"),
        ("M",  "Układ mięśniowo-szkieletowy"),
        ("N",  "Ośrodkowy układ nerwowy"),
        ("P", "Leki przeciwpasożytnicze, owadobójcze i repelenty"),
        ("R",  "Układ oddechowy"),
        ("S",  "Narządy wzroku i słuchu"),
        ("V",  "Różne")
    )
    name = models.CharField(choices=NAME, max_length=128)

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

