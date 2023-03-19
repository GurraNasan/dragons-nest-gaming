from django.db.models import Avg
from rating.models import Rating
from .models import Product


def get_product_rating(product_id):
    rating = Rating.objects.all()
    product_rating = rating.filter(product_id=product_id)
    return product_rating


def get_average_rating(product_id):
    ratings = Rating.objects.all()
    product_ratings = ratings.filter(product_id=product_id)
    get_avg_rating = product_ratings.aggregate(Avg('rating'))

    if get_avg_rating['rating__avg'] is not None:
        rating = round(get_avg_rating['rating__avg'], 1)
        return rating


def get_average_rating_list(products):
    ratings = Rating.objects.all()
    rating_aggregates = []
    for product in products:
        filtered_ratings = ratings.filter(product=product)
        get_avg_rating = filtered_ratings.aggregate(Avg('rating'))
        if get_avg_rating['rating__avg'] is not None:
            newdict = {
                "product": product.name,
                "rating": round(get_avg_rating['rating__avg'], 1),
            }
            rating_aggregates.append(newdict)
    return rating_aggregates
