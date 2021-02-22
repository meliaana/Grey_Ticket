from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from booth.models import Order
from .forms import UserRegisterForm, BalanceForm
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


@login_required()
def profile(request):
    orders = Order.objects.filter(user=request.user)

    return render(request, "user/profile.html", context={'orders': orders})


@login_required
def add_balance(request):
    form = BalanceForm

    if request.method == 'POST':
        form = BalanceForm(request.POST)
        if form.is_valid():
            user = request.user
            user.balance = form.cleaned_data.get("balance")
            user.save()
            return redirect('profile')

    return render(request, template_name='user/add-balance.html', context={'form': form})
