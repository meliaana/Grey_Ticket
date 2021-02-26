from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, FormView

from .models import Ticket, Order

from django.shortcuts import render, redirect

from booth.forms import TicketForm, OrderForm


class AddTicketVIew(FormView):
    form_class = TicketForm
    template_name = 'add-ticket.html'

    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST)

        if form.is_valid():
            form.save()
            # messages.success(request, f'success')

        return HttpResponse('Ticket has been added ')


class AddOrderView(LoginRequiredMixin, FormView):
    form_class = OrderForm
    template_name = 'add-order.html'

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'success')


class TicketListView(ListView):
    model = Ticket
    template_name = "tickets-listing.html"
    paginate_by = 2


def ticket_detail_view(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    user = request.user

    form = OrderForm

    if request.method == 'POST':
        if ticket.price <= user.balance:
            order = Order(user=user, ticket=ticket)
            order.save()
            user.balance -= ticket.price
            user.save()
            return redirect('profile')
        else:
            messages.error(request, 'Sorry, You dont have enough money!')

    return render(request, "ticket-detail.html", context={'ticket': ticket})
