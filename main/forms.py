from django import forms
from main.models import Rating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('review', 'ratings')