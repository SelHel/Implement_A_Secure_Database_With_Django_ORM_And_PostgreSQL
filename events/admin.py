from django.contrib import admin
from django.forms import ModelForm
from contracts.models import Contract

from events.models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            'name',
            'contract',
            'support_contact',
            'is_finished',
            'attendees',
            'event_date',
            'notes'
            )

    def save(self, commit=True):
        event = super().save(commit=False)
        event.client = event.contract.client
        if commit:
            event.save()
        return event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventForm
    list_display = (
        'id',
        'name',
        'client',
        'contract',
        'support_contact',
        'is_finished',
        'attendees',
        'event_date',
        'notes'
    )
    search_fields = ('name', 'client__company_name')
    list_filter = ('contract', 'support_contact', 'is_finished')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "contract":
            kwargs["queryset"] = Contract.objects.filter(is_signed=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
