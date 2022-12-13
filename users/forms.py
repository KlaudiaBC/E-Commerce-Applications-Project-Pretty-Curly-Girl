from django import forms
import datetime
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Add customised User Creation Form
    which will be updating automatically
    when User set the request
    """
    class Meta:
        model = UserProfile
        fields = ('user', 'email', 'birthdate')

    def __init__(self, *args, **kwargs):
        """
        Add customised django field for the input
        """
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['birthdate'].widget.attrs['class'] = 'form-control'
