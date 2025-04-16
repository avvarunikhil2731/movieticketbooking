from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Booking
class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': DateInput(),
        }
        labels = {
            'patient_name': "Patient Name",
            'patient_phone': "Patient Phone :",
            'patient_email': "Patient Email :",
            'doc_name': "Doctor Name :",
            'booking_date': "Booking Date :",
        }

    def clean_booking_date(self):
        booking_date = self.cleaned_data['booking_date']
        
        # Check if the booking date is in the past
        if booking_date < date.today():
            raise ValidationError("The date cannot be in the past! Please select a date from today onwards.")
        
        return booking_date