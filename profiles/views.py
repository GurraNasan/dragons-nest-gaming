from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def profile(request):
    """Display the user profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)
    orders = profile.order.all()
    template = 'profiles/profile.html'
    context = {
        'orders': orders,
        'form': form
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order {order.order_number}. \
            A confirmation email was sent to {order.email} on {order.date}'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
