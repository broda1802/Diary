from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import CustomUser
admin.site.register(CustomUser)
admin.site.register(User)