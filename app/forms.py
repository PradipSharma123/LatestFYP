
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class Availability_rooms(forms.Form):
    check_in = forms.DateTimeField(
        required=True, widget=DateInput, input_formats=["%Y-%m-%d", ])  # you can input any date time module you like from the djano date and time documentation
    check_out = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%d", ], widget=DateInput)  # from the official django documentation go the input format that you required
