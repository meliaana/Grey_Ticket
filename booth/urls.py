from django.urls import path

from booth.views import add_ticket, add_order

urlpatterns = [
    path('ticket/', add_ticket, name='add-ticket'),
    path('order/', add_order, name='add-order'),
]