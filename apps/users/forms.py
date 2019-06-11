"""User forms."""
# Django
from django import forms

class ProfileForm(forms.Form):
    """Profile information form."""
    # Controller type update
    website = forms.URLField(max_length=200, required=False)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)

class PictureForm(forms.Form):
    """Pircture form."""
    picture = forms.ImageField(required=True)
