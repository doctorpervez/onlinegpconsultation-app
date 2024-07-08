from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):

    date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    
    class Meta:
        model = Appointment
        fields = ['clinician', 'date', 'reason']
        widgets = {
                'clinician': forms.Select(attrs={'class':'form-control'}),
                'reason': forms.TextInput(attrs={'class':'form-control'}),



            }   

