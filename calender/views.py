from django.shortcuts import render


def calender(request):
    """ A view for the calender"""
    return render(request, 'calender/calender.html')
