from django import forms
from .models import UserProfile, RefundView, ReviewProduct


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_city': 'Town or City',
            'default_address_line_1': 'Address Line 1',
            'default_address_line_2': 'Address Line 2',
        }

        self.fields['default_phone'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


class RefundForm(forms.ModelForm):
    class Meta:
        model = RefundView
        fields = ('reference', 'message', 'email',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'reference': 'Order Number',
            'message': 'Please, tell us what went wrong.',
            'email': 'Email Address',
        }


class ReviewForm(forms.ModelForm):
    """
    Define the Comment form fields
    """
    class Meta:
        """
        Add widgets in the meta class
        """
        model = ReviewProduct
        fields = ('body', 'author')
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Type your review here."}),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'review_author',
                'type': 'hidden'}),
        }
