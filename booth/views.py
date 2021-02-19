from pyexpat.errors import messages

from django.shortcuts import render

from booth.forms import TicketForm, OrderForm


def add_ticket(request):
    form = TicketForm()

    if request.method == 'POST':
        form = TicketForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print('saved')
            messages.success(request, f'success')

    return render(request, 'add-ticket.html', {'form': form})


def add_order(request):
    form = OrderForm()

    print(request.method)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request, f'success')

    return render(request, 'order.html', {'form': form})