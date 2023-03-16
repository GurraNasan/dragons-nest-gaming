from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from products.models import Product
from profiles.models import UserProfile


class Rating(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='p_ratings',
    )
    rating = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ],
        null=False,
        blank=False,

    )
    review_title = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    review = models.TextField(
        null=True,
        blank=True
    )
