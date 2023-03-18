from datetime import datetime
from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils.safestring import mark_safe

from .models import Event
from .utils import create_calender


class calender(ListView):
    """ A view for the calender"""
    model = Event
    template_name = 'calender/calender.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        date = get_date(self.request.GET.get('day', None))

        cal = create_calender(date.year, date.month)

        html_cal = cal.formatmonth(withyear=True)

        context['calender'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(d) in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()