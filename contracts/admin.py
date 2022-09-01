from django.contrib import admin
from django.forms import ModelForm

from contracts.models import Contract


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = ('name', 'client', 'is_signed', 'amount', 'payment_due')

    def save(self, commit=True):
        contract = super().save(commit=False)
        contract.sales_contact = self.cleaned_data['client'].sales_contact
        if commit:
            contract.save()
        return contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    form = ContractForm
    list_display = (
        'id',
        'name',
        'sales_contact',
        'client',
        'is_signed',
        'amount',
        'payment_due'
        )
    search_fields = ('client',)
    list_filter = ('client', 'sales_contact', 'is_signed')
