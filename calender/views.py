from datetime import datetime, timedelta, date
from django.shortcuts import (
    render,
    get_object_or_404,
    HttpResponseRedirect,
    reverse
)
from django.views.generic.list import ListView
from django.utils.safestring import mark_safe
import calendar

from .models import Event
from .utils import create_calender
from .forms import EventForm


class calendar_view(ListView):
    """ A view for the calender"""
    model = Event
    template_name = 'calender/calender.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('month', None))
        cal = create_calender(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)

        context = {
            'calendar': mark_safe(html_cal),
            'prev_month': prev_month(d),
            'next_month': next_month(d),
        }

        return context


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_date(req_day):
    if req_day:
        year, month = (int(d) for d in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calender:calendar'))
    return render(request, 'calender/event.html', {'form': form})
