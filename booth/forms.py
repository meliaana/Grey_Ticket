from django import forms
from .models import Ticket, Order


class TicketForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
    price = forms.DecimalField()

    class Meta:
        model = Ticket
        fields = ['name', 'start_date', 'end_date', 'price']


class OrderForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=Order.objects.all())
    ticket = forms.ModelChoiceField(queryset=Ticket.objects.all())

    class Meta:
        model = Order
        fields = ['user', 'ticket', ]
