from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile

from .models import Rating
from .forms import RatingForm


def rating(request):
    """
        A view to return the rating/reviews page
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    rating = Rating.objects.all()
    user_ratings = rating.filter(user_profile=profile)

    template = 'rating/rating.html'

    context = {
        'profile': profile,
        'user_ratings': user_ratings,
    }

    return render(request, template, context)
