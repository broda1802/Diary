from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from patientdiary.models import Patient
from .forms import AddUserAndPatientForm

# Create your views here.
from .models import CustomUser


class SignUpView(View):
    def get(self, request):
        form = AddUserAndPatientForm()
        return render(request, 'registration/signup.html', context={'form': form})

    def post(self, request):
        form = AddUserAndPatientForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(username=request.POST.get("username"),
                                                  email=request.POST.get("email"),
                                                  password=(request.POST.get("password1")))
            user.save()
            patient = Patient.objects.create(user=user)
            patient.save()
            return redirect('/login')
