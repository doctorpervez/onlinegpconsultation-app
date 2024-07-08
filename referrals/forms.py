from django import forms
from .models import Referral

class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['referred_to_clinician', 'specialty','title', 'reason']

        widgets = {
            'referred_to_clinician': forms.TextInput(attrs={"size": "40", 'class':'form-control'}),
            'specialty': forms.TextInput(attrs={'rows': 5,  'class':'form-control'}),
            'title': forms.TextInput(attrs={'rows': 5,  'class':'form-control'}),
            'reason': forms.Textarea(attrs={'rows': 5,  'class':'form-control'}),

        }

