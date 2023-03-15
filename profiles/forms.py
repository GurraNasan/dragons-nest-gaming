from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Address',
            'default_street_address2': 'Address',
            'default_postcode': 'Postal Code',
            'default_city': 'City',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True

        self.fields['default_full_name'].widget.attrs['aria-label'] = 'Full Name'
        self.fields['default_email'].widget.attrs['aria-label'] = 'Email Address'
        self.fields['default_phone_number'].widget.attrs['aria-label'] = 'Phone Number'
        self.fields['default_postcode'].widget.attrs['aria-label'] = 'Post Code'
        self.fields['default_city'].widget.attrs['aria-label'] = 'City'
        self.fields['default_street_address1'].widget.attrs[
            'aria-label'] = 'Street Address 1'
        self.fields['default_street_address2'].widget.attrs[
            'aria-label'] = 'Street Address 2'
        self.fields['default_country'].widget.attrs['aria-label'] = 'Country'

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
