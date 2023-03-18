from django.db import models
from django.urls import reverse


class Event(models.Model):
    """
        A model for the events to the calaneder
    """
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('calender:event_info', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
