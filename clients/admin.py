from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'phone',
        'mobile',
        'company_name',
        'sales_contact'
        )
    search_fields = ('first_name', 'last_name', 'email', 'company_name')
    list_filter = ('sales_contact',)
