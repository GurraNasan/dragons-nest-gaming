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


def add_rating(request):
    """
        A view to add rating and reviews
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            form.instance.user_profile = profile
            form.save()
            messages.success(request, 'Thanks! All worked')
            return redirect(reverse('add_rating'))
        else:
            messages.error(request, 'Failed, please try again')
    else:
        form = RatingForm()

    template = 'rating/add_rating.html'
    context = {
        'form': form,
    }

    return render(request, template, context)