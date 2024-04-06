from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
# from .models import Task
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('index')  # Redirect to the homepage or any other page
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'base/profile.html')