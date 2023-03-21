from django.contrib import admin

from .models import Event

list_display = (
    'title',
    'start_time',
    'end_time',
)

search_fields = (
    'title',
    'start_time',
    'end_time',
)

admin.site.register(Event)
