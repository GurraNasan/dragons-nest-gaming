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


def edit_rating(request, rating_id):
    """
        A view to edit rating and reviews
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    rating = get_object_or_404(Rating, pk=rating_id)
    if request.user != rating.user_profile.user:
        messages.error(
            request, 'You don´t have permission to edit this review'
        )
        return redirect('home')

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            form.instance.user_profile = profile
            form.save()
            messages.success(request, 'Thanks! All worked')
            return redirect('rating')
        else:
            messages.error(request, 'Failed, please try again')
    else:
        form = RatingForm(instance=rating)

    template = 'rating/edit_rating.html'
    context = {
        'form': form,
        'rating': rating,
    }

    return render(request, template, context)


def delete_rating(request, rating_id):
    """
        A view for delete rating and review
    """
    rating = get_object_or_404(Rating, pk=rating_id)
    if request.user != rating.user_profile.user:
        messages.error(
            request, 'You don´t have permission to delete this review'
        )
        return redirect('home')

    rating.delete()
    messages.success(request, 'Rating/Review successfully deleted')
    return redirect('rating')
