from django.contrib import admin
from .models import Product, Category, SubCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'available',
        'in_stock',
        'image',
    )

    ordering = ['name',]
    search_fields = ['name', 'category', 'price']


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory)
