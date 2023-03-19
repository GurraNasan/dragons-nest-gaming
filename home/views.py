from django.shortcuts import render


def index(request):
    """ A view for the indexpage"""
    return render(request, 'home/index.html')


def privacy(request):
    """ A view for the privacy policy"""
    return render(request, 'home/index.html')


def return_and_refund(request):
    """ A view for the return and refund policy"""
    return render(request, 'home/index.html')


def shipping(request):
    """ A view for the shipping policy"""
    return render(request, 'home/index.html')


def terms(request):
    """ A view for the term and conditions"""
    return render(request, 'home/index.html')