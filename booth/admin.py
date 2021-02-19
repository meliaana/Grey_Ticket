from django.contrib import admin
from .models import Ticket, Order

admin.site.register([Order])


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    exclude = ('code', )
