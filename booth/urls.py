from django.urls import path

from booth.views import AddTicketVIew, AddOrderView, ticket_detail_view, TicketListView

urlpatterns = [
    path('add-ticket/', AddTicketVIew.as_view(), name='add-ticket'),
    path('add-order/', AddOrderView.as_view(), name='add-order'),
    path('ticket-detail/<int:pk>/', ticket_detail_view, name='ticket-detail'),
    path('', TicketListView.as_view(), name='all-tickets')
]