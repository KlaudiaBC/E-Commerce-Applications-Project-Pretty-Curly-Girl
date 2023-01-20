from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone',
                  'address_line_1', 'address_line_2',
                  'city', 'postcode', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'phone': 'Phone Number',
            'email': 'Email Address',
            'postcode': 'Postal Code',
            'city': 'City',
            'address_line_1': 'Street Name',
            'address_line_2': 'House Number',
        }

        """
        Start the cursor on the full_name field when user loads the page
        """
        self.fields['full_name'].widget.attrs['autofocus'] = True

        """
        Add star to the placeholder if the field is required
        """
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
