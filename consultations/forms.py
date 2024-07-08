from django import forms
from .models import Consultation, Test, TestChoice


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['diagnosis', 'notes']
        widgets = {
            'diagnosis': forms.TextInput(attrs={"size": "40", 'class':'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 5,  'class':'form-control'}),
        }



class TestForm(forms.ModelForm):
    test_choices = forms.ModelMultipleChoiceField(
        queryset=TestChoice.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        required=True  # Ensure the field is required
    )

    class Meta:
        model = Test
        fields = ['test_choices']

