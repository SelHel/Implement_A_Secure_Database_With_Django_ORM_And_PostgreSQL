from django.contrib import admin

from contracts.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sales_contact',
        'client',
        'is_signed',
        'amount',
        'payment_due'
        )
