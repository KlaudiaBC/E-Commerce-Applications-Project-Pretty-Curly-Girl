from django import forms
from .models import UserProfile, Address


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
            'email': 'Email Address',
            'birth_date': 'Date of birth',
        }

        self.fields['default_phone'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] =\
                'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ('user_profile',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_postcode': 'Postal Code',
            'default_city': 'Town or City',
            'default_address_line_1': 'Street Address 1',
            'default_address_line_1': 'Street Address 2',
        }

        self.fields['default_postcode'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] =\
                'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
