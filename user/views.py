from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.utils.translation import gettext_lazy as _


def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created for! ')
            return redirect('profile')

    return render(request, "user/register.html", context={"form": form})


def profile(request):
    return render(request, "user/profile.html")