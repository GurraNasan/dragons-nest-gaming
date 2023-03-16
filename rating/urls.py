from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.rating,
        name="rating"
    ),
    path(
        'add/',
        views.add_rating,
        name="add_rating",
    ),
]
