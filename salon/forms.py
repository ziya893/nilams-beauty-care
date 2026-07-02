from django import forms
from django.utils import timezone

from .models import Appointment, Service


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'full_name', 'phone_number', 'email',
            'service', 'preferred_date', 'preferred_time', 'message',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Your full name', 'class': 'form-control',
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': '10-digit mobile number', 'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'you@example.com (optional)', 'class': 'form-control',
            }),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'preferred_date': forms.DateInput(attrs={
                'type': 'date', 'class': 'form-control',
            }),
            'preferred_time': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={
                'rows': 3, 'placeholder': 'Tell us anything else we should know (optional)',
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.filter(is_active=True)
        self.fields['service'].empty_label = "General enquiry / not sure yet"
        self.fields['email'].required = False
        self.fields['message'].required = False

    def clean_preferred_date(self):
        preferred_date = self.cleaned_data['preferred_date']
        if preferred_date < timezone.localdate():
            raise forms.ValidationError("Please choose today's date or a future date.")
        return preferred_date

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number'].strip()
        digits = ''.join(ch for ch in phone_number if ch.isdigit())
        if len(digits) < 10:
            raise forms.ValidationError("Please enter a valid 10-digit mobile number.")
        return phone_number
