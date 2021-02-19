from django.shortcuts import render
from .forms import UserRegisterForm


def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "user/profile.html", context={"form": form})
