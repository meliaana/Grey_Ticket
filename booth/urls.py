from django.urls import path

from booth.views import add_ticket, add_order, tickets_list_view, ticket_detail_view

urlpatterns = [
    path('ticket/', add_ticket, name='add-ticket'),
    path('order/', add_order, name='add-order'),
    path('ticket-detail/<int:pk>/', ticket_detail_view, name='ticket-detail'),
    path('', tickets_list_view, name='all-tickets')
]