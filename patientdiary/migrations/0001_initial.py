# Generated by Django 3.2.8 on 2021-10-20 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('street', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('medical_specialization', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('leaflet', models.TextField()),
                ('dosage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('action', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('Pesel', models.IntegerField(null=True, unique=True)),
                ('phone', models.IntegerField(null=True)),
                ('my_history', models.TextField(null=True)),
                ('clinic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patientdiary.clinic')),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('street', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('opening_hours', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Substance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientDrug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientdiary.drugs')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientdiary.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientdiary.disease')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientdiary.patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='disease',
            field=models.ManyToManyField(blank=True, through='patientdiary.PatientDisease', to='patientdiary.Disease'),
        ),
        migrations.AddField(
            model_name='patient',
            name='drug',
            field=models.ManyToManyField(blank=True, through='patientdiary.PatientDrug', to='patientdiary.Drugs'),
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patientdiary.group')),
            ],
        ),
        migrations.AddField(
            model_name='drugs',
            name='groups',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientdiary.group'),
        ),
        migrations.AddField(
            model_name='drugs',
            name='substances',
            field=models.ManyToManyField(to='patientdiary.Substance'),
        ),
    ]
