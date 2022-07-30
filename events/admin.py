from django.contrib import admin

from events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
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
