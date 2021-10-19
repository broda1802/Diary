from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Patient)
admin.site.register(Disease)
admin.site.register(Substance)
admin.site.register(Drugs)
admin.site.register(Group)
admin.site.register(Clinic)
admin.site.register(Pharmacy)
admin.site.register(Doctor)

