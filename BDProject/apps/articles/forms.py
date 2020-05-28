from django import forms
from .models import Photo

class SimpleAddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'description', 'care', 'photo')

