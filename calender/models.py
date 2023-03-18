from django.db import models
from django.urls import reverse


class Event(models.Model):
    """
        A model for the events to the calaneder
    """
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    start_time = models.DateTimeField(null=False, blank=False)
    end_time = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('calender:edit_event', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
