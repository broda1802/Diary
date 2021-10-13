# Generated by Django 3.2.8 on 2021-10-13 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('dosage', models.IntegerField()),
                ('action', models.CharField(max_length=128)),
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
                ('substance_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('Pesel', models.IntegerField(unique=True)),
                ('phone', models.IntegerField()),
                ('my_history', models.TextField()),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientdiary.clinic')),
                ('disease', models.ManyToManyField(to='patientdiary.Disease')),
                ('drug', models.ManyToManyField(to='patientdiary.Drugs')),
            ],
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
            name='substances',
            field=models.ManyToManyField(to='patientdiary.Substance'),
        ),
    ]
