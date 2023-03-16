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
    path(
        'edit/<int:rating_id>',
        views.edit_rating,
        name="edit_rating"
        ),
    path(
        'delete/<int:rating_id>',
        views.delete_rating,
        name="delete_rating"
    ),
]
