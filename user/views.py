from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Q
from django.shortcuts import render, redirect
from datetime import datetime

from django.views.generic import FormView

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
    user = request.user
    orders = Order.objects.filter(user=user)

    month = datetime.now().month
    year = datetime.now().year

    return render(request, "user/profile.html", context={'orders': orders})


class AddBalanceView(LoginRequiredMixin, FormView):
    form_class = BalanceForm
    template_name = 'user/add-balance.html'

    def post(self, request, *args, **kwargs):
        form = BalanceForm(request.POST)
        if form.is_valid():
            user = request.user
            user.balance += form.cleaned_data.get("balance")
            user.save()
            return redirect('profile')

