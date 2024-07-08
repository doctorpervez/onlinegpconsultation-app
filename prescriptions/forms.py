# prescriptions/forms.py
from django import forms
from .models import Prescription

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['medication', 'dosage', 'instructions']

        widgets = {
            'medication': forms.TextInput(attrs={"size": "40", 'class':'form-control'}),
            'dosage': forms.TextInput(attrs={'rows': 5,  'class':'form-control'}),
            'instructions': forms.Textarea(attrs={'rows': 5,  'class':'form-control'}),
        }
