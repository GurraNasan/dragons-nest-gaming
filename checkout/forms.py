from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address1',
            'street_address2',
            'city',
            'postcode',
            'country',
        )


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    placeholder = {
        'full_name': 'Full Name',
        'email': 'Email Address',
        'phone_number': 'Phone Number',
        'street_address1': 'Address',
        'street_address2': 'Address',
        'postcode': 'Postal Code',
        'city': 'City',
    }

    self.fields['full_name'].widget.attrs['autofocus'] = True
    self.fields['full_name'].widget.attrs['aria-label'] = 'Full Name'
    self.fields['email'].widget.attrs['aria-label'] = 'Email Address'
    self.fields['phone_number'].widget.attrs['aria-label'] = 'Phone Number'
    self.fields['postcode'].widget.attrs['aria-label'] = 'Post Code'
    self.fields['city'].widget.attrs['aria-label'] = 'City'
    self.fields['street_address1'].widget.attrs[
        'aria-label'] = 'Street Address 1'
    self.fields['street_address2'].widget.attrs[
        'aria-label'] = 'Street Address 2'
    self.fields['country'].widget.attrs['aria-label'] = 'Country'

    for field in self.fields:
        if field != 'country':
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        self.fields[field].label = False
