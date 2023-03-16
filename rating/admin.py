from django.contrib import admin

from .models import Rating


class RatingAdmin(admin.ModelAdmin):

    list_display = ( 
        'product',
        'user_profile',
        'rating',
        'review_title',
    )


admin.site.register(Rating, RatingAdmin)
