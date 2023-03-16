from django.shortcuts import render


def rating(request):
    """
        A view to return the rating/reviews page
    """

    template = 'rating/rating.html'
    context = {}

    return render(request, template, context)
