from django.db import models


# Borrowed code from the boutiq ado project in the Code institute course
class Category(models.Model):
    """ main category, gametype, merch """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200, unique=True)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SubCategory(models.Model):
    """ Models for deals or new arrivals """
    class Meta:
        verbose_name_plural = 'Subcategories'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Models for the products """
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    sub_category = models.ForeignKey(
        'SubCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=240)
    sku = models.CharField(max_length=240, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    available = models.DecimalField(max_digits=3, decimal_places=0)
    new_arrival = models.BooleanField(default=False, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
