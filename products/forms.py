from django import forms

from .widgets import CustomClearableFileInput
from .models import Product, Category, SubCategory


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Product Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        """
        Add aria labels to fields for accessibility
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # subcategories = SubCategory.objects.all()
        friendly_name_c = [
            (c.id, c.get_friendly_name()) for c in categories
        ]
        # friendly_name_s = [
        #     (s.id, s.get_friendly_name()) for s in subcategories
        # ]

        self.fields['category'].choices = friendly_name_c
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'

        # self.fields['subcategory'].choices = friendly_name_s
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'rounded-0'

        self.fields['image'].widget.attrs['aria-label'] = 'Select a Product Image'