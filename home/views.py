from django.shortcuts import render


def index(request):
    """ A view for the indexpage"""
    return render(request, 'home/index.html')
