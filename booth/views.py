from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Ticket, Order

from django.shortcuts import render, redirect

from booth.forms import TicketForm, OrderForm


def add_ticket(request):
    form = TicketForm()

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, f'success')

    return render(request, 'add-ticket.html', {'form': form})


@login_required
def add_order(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'success')

    return render(request, 'order.html', {'form': form})


def tickets_list_view(request):
    tickets = Ticket.objects.all()

    paginator = Paginator(tickets, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "tickets-listing.html",
        context={
            'tickets': tickets,
            'page_obj': page_obj,
        },

    )


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
