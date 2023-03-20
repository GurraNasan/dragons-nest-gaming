from django.shortcuts import render


def index(request):
    """ A view for the indexpage"""
    return render(request, 'home/index.html')


def privacy(request):
    """ A view for the privacy policy"""
    return render(request, 'home/privacy_policy.html')


def return_and_refund(request):
    """ A view for the return and refund policy"""
    return render(request, 'home/return_and_refund_policy.html')


def terms(request):
    """ A view for the term and conditions"""
    return render(request, 'home/term_and_conditions.html')