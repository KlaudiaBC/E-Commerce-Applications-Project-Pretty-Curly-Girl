"""
Define and customise Forms
"""
from django import forms
from .models import UserReview


class ReviewForm(forms.ModelForm):
    """
    Define the Comment form fields
    """
    class Meta:
        """
        Add widgets in the meta class
        """
        model = UserReview
        fields = ('body', 'author')
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Type your review here."}),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Type your name here."})
        }
