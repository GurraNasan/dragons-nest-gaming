from django import forms
from .models import Rating
from profiles.models import UserProfile


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['user_profile']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
