from datetime import date
from django import forms

class CustomDatePickerWidget(forms.DateInput):
    """ Create a custom datepicker widget."""
    DATE_INPUT_WIDGET_REQUIRED_FORMAT = '%Y-%m-%d'

    def __init__(self, attrs={}, format=None):
        """Constructor for class CustomDatePickerWidget."""
        attrs.update(
            {
                'class': 'form-control',
                'type': 'date',
            }
        )
        self.format = format or self.DATE_INPUT_WIDGET_REQUIRED_FORMAT
        super().__init__(attrs, format=self.format)



class PastCustomDatePickerWidget(CustomDatePickerWidget):
    """
    Set maximum date as today to prevent users from 
    choosing future dates as birthday.
    """

    def __init__(self, attrs={}, format=None):
        attrs.update(
            {
                'max': date.today(),
            }
        )
        super().__init__(attrs, format=format)